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
$ pip install -r requirements.txt
```

3. Set environment variables
```
$ export AIRFLOW_HOME=$PWD
$ airflow upgradedb
```

4. List Airflow DAGs 
```
$ airflow list_dags

-------------------------------------------------------------------
DAGS
-------------------------------------------------------------------
...
github_poll_trigger
...

```
5. Setup Airflow variables
```
$ airflow variables -s ENVIRONMENT CI
$ airflow variables -s S3_BUCKET [your s3 bucket]
$ airflow variables -s AWS_ACCESS_KEY_ID [your aws access key id]
$ airflow variables -s AWS_SECRET_ACCESS_KEY [your aws secret key]
$ airflow variables -s SNOWFLAKE_CONNECTION SNOWFLAKE_DEV

```
6. Run test
```
$ airflow test github_poll_trigger check_commits_dromic_covid_19_sitreps 2020-04-04
```

6. Start coding
```
$ jupyter-notebook
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
$ airflow trigger_dag -e 2020-04-04 github_poll_tirgger
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

