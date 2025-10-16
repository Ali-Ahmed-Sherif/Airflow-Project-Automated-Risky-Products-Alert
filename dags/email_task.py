from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.email_operator import EmailOperator
from datetime import datetime, timedelta
import pyodbc
import csv

def connect_to_sqlserver():
    conn = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=sqlserver,1433;"
    "DATABASE=Sales_DataMart_2022;"
    "UID=sa;"
    "PWD=Vortex2025;"
    "TrustServerCertificate=yes;"
)

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products_summary WHERE product_status_flag='Risky (Negative Profit)'")
    rows = cursor.fetchall()
    
    with open("/opt/airflow/shared/risky_products.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([column[0] for column in cursor.description])  # header
        writer.writerows(rows)

    cursor.close()
    conn.close()

with DAG(
    dag_id="email_task",
    start_date=datetime(2025, 10, 16),
    schedule_interval=timedelta(days=10),
    catchup=False
) as dag:

    task_sql = PythonOperator(
        task_id="task_sql",
        python_callable=connect_to_sqlserver
    )

    task_mail = EmailOperator(
        task_id="task_mail",
        to="####",
        subject="Risky Products📛",
        html_content='<h3>Review these products and the reason behind the negative net profit</h3>',
        files=["/opt/airflow/shared/risky_products.csv"]
    )

task_sql >> task_mail
