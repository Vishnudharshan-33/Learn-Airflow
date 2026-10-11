from datetime import datetime
from airflow import DAG
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.sdk import task


@task
def read_file():
    hook = S3Hook(aws_conn_id='minioS3_Conn')
    content = hook.read_key(key='data.csv', bucket_name='airflow')
    print(content[:500])

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2026, 10, 10),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

with DAG(
    dag_id='dag_with_minioS3_v01',
    default_args=default_args,
    schedule='@daily',
    catchup=False,
) as dag:
    task1 = S3KeySensor(
        task_id='sensor_minioS3_v01',
        bucket_name='airflow',
        bucket_key='data.csv',
        aws_conn_id='minioS3_Conn',
        mode='reschedule',
        poke_interval=30,
        timeout=600,
    )
    task1 >> read_file()   