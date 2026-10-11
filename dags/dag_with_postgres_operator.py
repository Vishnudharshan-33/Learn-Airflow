from datetime import datetime
from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2026, 10, 7),
}   

with DAG(
    dag_id = 'postgres_operator_v02',
    default_args = default_args
) as dag:
    task1 = SQLExecuteQueryOperator(
        task_id = 'create_table',
        conn_id = 'postgres_localhost',
        sql= """
            create table if not exists dag_runs(
                dt date,
                dag_id character varying,
                primary key (dt, dag_id)
                )
        """
    )

    task2 = SQLExecuteQueryOperator(
        task_id = 'insert_into_table',
        conn_id = 'postgres_localhost',
        sql = """
            insert into dag_runs(dt, dag_id) values ( '{{ ds }}', '{{ dag.dag_id }}' )"""
    )

    task1 >> task2
