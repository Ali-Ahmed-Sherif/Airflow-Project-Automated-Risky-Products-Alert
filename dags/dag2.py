from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

def age():
    for i in range(3):
        print(f"bash you have {i} age")
with DAG(
    dag_id='dag2',
    start_date=datetime(2025,9,30),
    schedule_interval=timedelta(minutes=1),
    catchup=False
) as dag:
    task_bash_1 = BashOperator(
        task_id ="dag2_bash_1",
        bash_command='echo "hello bash"'

    )
    task_python_1 = PythonOperator(
        task_id="dag2_python_1",
        python_callable=age
    )

    task_bash_1 >> task_python_1