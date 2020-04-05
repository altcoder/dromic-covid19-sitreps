# Local Development

1. Clone this repo.

```
$ git clone https://github.com/[GITHUB_USERNAME]/[REPO_NAME].git
$ cd [REPO_NAME]
```

2. Setup virtualenv or Conda environment and install dependencies

``` 
$ conda create --prefix ./conda-env
$ conda activate ./conda-env
$ pip install -r requirements-airflow.txt
$ pip install -r requirements.txt
```

3. Setup environment
```
$ cp airflow-vars-sample.json airflow-vars.json
[edit airflow-vars.json]
$ source init.sh

```

4. List Airflow DAGs (testing) 
```
$ airflow list_dags

-------------------------------------------------------------------
DAGS
-------------------------------------------------------------------
...
github_poll_trigger
...

```
5. Run test DAG
```
$ airflow test github_poll_trigger check_commits_dromic_covid_19_sitreps 2020-04-04
```

6. Start coding
```
$ jupyter-lab
```

# Integration Test

1. Unpause dags 
```
$ airflow unpause [dag_id]
```
2. Run scheduler (and optionally web server for monitoring)
```
$ airflow scheduler
$ airflow webserver
```

3. Trigger dag 
```
$ airflow trigger_dag -e 2020-04-04 github_poll_trigger
```

# Production Deployment (Astronomer)

1. Initialize project
```
$ astro dev init
```

2. Open web airflow
```
$ astro dev start
```

3. Deploy
```
$ astro deploy
```

