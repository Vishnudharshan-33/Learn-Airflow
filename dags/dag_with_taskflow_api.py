from airflow.decorators import dag, task
from datetime import datetime, timedelta

default_args = {
    'owner': 'vishnu',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}



@dag(dag_id='dag_with_taskflow_api_v01', default_args=default_args,start_date=datetime(2026, 10, 4), schedule='@daily' )
def hello_world_etl():
    @task(multiple_outputs=True)
    def get_name():
        return {
            'first_name': 'Vishnu',
            'last_name': 'Dharshan'
        }

    @task()
    def get_age():
        return 23

    @task()
    def greet(first_name, last_name, age):
        print(f"Hello {first_name} {last_name}, you are {age}!")

    name_dict = get_name()
    age = get_age()
    greet(name_dict['first_name'], name_dict['last_name'],age)


greet_dag = hello_world_etl()

