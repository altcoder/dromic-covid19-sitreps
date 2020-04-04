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
4. Test airflow CLI 
```
$ airflow list_dags

-------------------------------------------------------------------
DAGS
-------------------------------------------------------------------
...
github_poll_trigger
...
```


