from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG("kaggle_dag", start_date=datetime(year=2021, month=8, day=11),
    schedule_interval='45 11 * * *', catchup=False) as dag:

    extract_data = BashOperator(
        task_id='extract_data', 
        bash_command='python /opt/airflow/dags/extract_data.py',
    )

    load_data = BashOperator(
        task_id='load_data', 
        bash_command='python /opt/airflow/dags/load_data.py',
    )

    extract_data>>load_data
