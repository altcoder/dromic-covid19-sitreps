import airflow
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import BranchPythonOperator
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.configuration import conf
import logging
import json
import requests
import os
import glob
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

DAGS_FOLDER = conf.get('core', 'dags_folder')

with open( DAGS_FOLDER + "/../config/refresh_schedules.json", 'r') as f:
    schedules = json.load(f)

args = {
    'owner': 'admin',
    'start_date': datetime(2020, 4, 11),
    'catchup_by_default': False
}

def download_recent_files(**kwargs):
    name =kwargs.get('name')
    url =kwargs.get('url')

    # List all available files
    sitreps = [os.path.basename(x) for x in glob.glob(DAGS_FOLDER + '/../datasets/sitreps/*.docx')]

    logging.info('Loading new data from %s' % url)

    # Need User-Agent header to be able to fetch data
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(url, headers=headers, allow_redirects=True)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('div', class_='wp-block-file')

    is_new_files = False
    for result in results:
        link_elem = result.find('a')
        link = link_elem['href']
        filename = os.path.basename(link)
        if filename not in sitreps:
            print(link, filename)
            docx = requests.get(link, headers=headers, allow_redirects=True)
            open(DAGS_FOLDER + '/../datasets/sitreps/%s' % filename, 'wb').write(docx.content)
            logging.info('New file %s downloaded' % filename)
            is_new_files = True

    if is_new_files:
        logging.info('New data available. Running %s.' % name.lower())
        return f"trigger_{name.lower()}_fas"
    else:
        return "stop"

dag = DAG(
    dag_id='webpage_poll_trigger',
    default_args=args,
    schedule_interval="@daily"
)


with dag:

    stop_op = DummyOperator(task_id='stop', trigger_rule="all_done", dag=dag)

    start_op = DummyOperator(task_id='start', dag=dag)

    for name, url in schedules["sources"].items():
        if url.startswith('https://dromic'):
            check_webpage_op = BranchPythonOperator(
                task_id=f'check_webpage_{name.lower()}',
                python_callable=download_recent_files,
                provide_context=True,
                op_kwargs={"name": name, "url": url},
                trigger_rule="all_done",
                dag=dag,
            )
            trigger_etl_fas_op = TriggerDagRunOperator(
                task_id=f"trigger_{name.lower()}_fas",
                trigger_dag_id=f'etl_{name}_fas',
                dag=dag
            )
            trigger_etl_coa_op = TriggerDagRunOperator(
                task_id=f"trigger_{name.lower()}_coa",
                trigger_dag_id=f'etl_{name}_coa',
                dag=dag
            )
            start_op >> check_webpage_op
            check_webpage_op >> trigger_etl_fas_op >> trigger_etl_coa_op
            check_webpage_op >> stop_op
            trigger_etl_coa_op >> stop_op
