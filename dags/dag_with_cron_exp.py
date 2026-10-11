from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'vishnu',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='dag_with_cron_exp_v01',
    default_args=default_args,
    start_date=datetime(2026,9,28),
    schedule='* 6 * * 1,3',

)as dag:
    task = BashOperator(
        task_id = 'Helloworld',
        bash_command = 'echo "Hello world"'
    )
    task