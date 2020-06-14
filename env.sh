conda deactivate
conda activate ./conda-env

export AIRFLOW_HOME=$PWD

# Modify airflow-vars-sample.json and change the credentials based on your setup
airflow variables -i airflow-vars.json
