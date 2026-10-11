from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args= {
    'owner': 'vishnu',
    'depends_on_past': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=3)
}

with DAG(
    dag_id= 'our_first_dag',
    default_args= default_args,
    description= 'My first DAG',
    schedule='@daily',
    start_date= datetime(2024, 6, 1)
) as dag:
    task1= BashOperator(
        task_id= 'task-1',
        bash_command= 'echo "hello world"'
    )
    task2 = BashOperator(
        task_id= 'task-2',
        bash_command= 'echo "task 2"'   
    )
    task3 = BashOperator(
        task_id= 'task-3',
        bash_command= 'echo "Goodbye world"'
    )

    #method 1
    #task1 >> task2 >> task3

    #method 2
    # task1.set_downstream(task2)
    # task2.set_downstream(task3)

    #method 3
    task1 >> [task2, task3]