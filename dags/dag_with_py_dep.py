from datetime import datetime
from airflow import DAG 
from airflow.operators.python import PythonOperator


def get_sklearn_version():
    import sklearn
    return sklearn.__version__


with DAG(
    dag_id = 'dag_with_py_dep_v01',
    start_date = datetime(2026, 10, 7),
    schedule = '@daily'
) as dag:
    task1 = PythonOperator(
        task_id = 'get_sklearn_version',
        python_callable = get_sklearn_version
    )
    task1