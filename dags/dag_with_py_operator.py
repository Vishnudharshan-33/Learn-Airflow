from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'vishnu',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

def greet(ti, age):
    first_name = ti.xcom_pull(task_ids='get_name_task',key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name_task', key='last_name')
    print(f"Hello {first_name} {last_name}, you are {age}!")

def get_name(ti):
    ti.xcom_push(key='first_name', value='Vishnu')
    ti.xcom_push(key='last_name', value='Dharshan')


with DAG(
    dag_id='dag_with_py_operator_v05',
    default_args=default_args,
    description='A simple DAG with PythonOperator',
    schedule='@daily',
    start_date=datetime(2026, 10, 4)
) as dag:
    task1 = PythonOperator(
        task_id='greet_task',
        python_callable=greet,
        op_kwargs={'age':23}
    )

    task2 = PythonOperator(
        task_id='get_name_task',
        python_callable=get_name
    )

    task2 >> task1