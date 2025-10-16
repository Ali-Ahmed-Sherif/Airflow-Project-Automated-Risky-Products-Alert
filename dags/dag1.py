from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def hello_airflow():
    print("Hello Airflow! This is my first DAG.")

with DAG(
    dag_id='dag1',
    start_date=datetime(2025, 9, 28),
    schedule_interval=timedelta(minutes=1),
    catchup=False
) as dag:

    task_hello = PythonOperator(
        task_id='say_hello',
        python_callable=hello_airflow
    )
