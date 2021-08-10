from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator, task

with DAG("my_dag", start_date=datetime(year=2021, month=8, day=10),
    schedule_interval='45 11 * * *', catchup=False) as dag:

    import_lib = BashOperator(
        task_id='import_lib', 
        bash_command='apt-get update && apt-get install -y --no-install-recommends unixodbc-dev unixodbc libpq-dev ',
    )

    extract_data = BashOperator(
        task_id='extract_data', 
        bash_command='python /opt/airflow/dags/extract_data.py',
    )

    load_data = BashOperator(
        task_id='load_data', 
        bash_command='python /opt/airflow/dags/load_data.py',
    )

    import_lib>>extract_data>>load_data
