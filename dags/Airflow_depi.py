from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
import random
from datetime import datetime, timedelta

def save_file():
    number = random.randint(1,100)
    with open("/opt/airflow/shared/tmp/random.txt", "w") as f:
        f.write(str(number))

def print_name():
    print("wassup ali")

with DAG(
    dag_id="Airflow_Depi",
    start_date=datetime(2025, 10, 16),
    schedule_interval=timedelta(minutes=1),
    catchup=False
) as dag:

    task_date = BashOperator(
        task_id="task1",
        bash_command="date"
    )

    task_msg = PythonOperator(
        task_id="task2",
        python_callable=print_name
    )

    task_saving = PythonOperator(
        task_id="task3",
        python_callable=save_file
    )

    task_date >> task_msg >> task_saving
