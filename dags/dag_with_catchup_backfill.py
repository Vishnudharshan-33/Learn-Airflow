from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator
from airflow import DAG

default_args = {
    'owner': 'vishnu',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='dag_with_catchup_backfill_v02',
    default_args=default_args,
    start_date=datetime(2026, 10, 1),
    schedule='@daily',
    catchup=False
) as dag:
    task = BashOperator(
        task_id = 'Hello_World',
        bash_command = 'echo "hello world"'
    )
    task