# DROMIC COVID19 SitReps Data

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://raw.githubusercontent.com/altcoder/[REPO_NAME]/master/LICENSE)
![Airflow/DAG](https://github.com/altcoder/dromic-covid19-sitreps/workflows/Airflow/DAG/badge.svg)

Generate machine readable data on DSWD DROMIC COVID-19 SitReps in the Philippines.

[Google Sheet](https://docs.google.com/spreadsheets/d/1eS44h4aIvjXspFFnTd3rEepKaL0nQNcMX_Z8Jnfclp4/edit?usp=sharing)

## Quickstart

1. Clone this repo.

```
$ git clone https://github.com/[GITHUB_USERNAME]/[REPO_NAME].git
$ cd [REPO_NAME]
```

2. Setup your Python dependencies

``` 
$ pip install -r requirements-airflow.txt
$ pip install -r requirements.txt
```

3. Set environment variables

```
$ export AIRFLOW_HOME=$PWD
$ airflow upgradedb
```

4. Run
```
$ airflow etl_dromic_covid_19_sitreps execute_notebook 2020-04-04
```

5. View generated files in output directory 

```
$ ls output
```

## Development

This project uses Apache Airflow to run Python Notebooks as jobs. Follow [this instuctions](docs/SETUP.md) to setup your local development environment. 

#### Official Source 

[DSWD DROMIC Virtual OpCen Coronavirus Sitreps](https://dromic.dswd.gov.ph/coronavirus-disease-covid-19-31-dec-2019/)


## CONTRIBUTING

Contributions are always welcome, no matter how large or small. Before contributing,
please read the [code of conduct](.github/CODE_OF_CONDUCT.md).
