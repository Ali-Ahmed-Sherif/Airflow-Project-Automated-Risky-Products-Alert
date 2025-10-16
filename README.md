
#  Airflow Project: Automated Risky Products Alert

## Project Overview
This project demonstrates the use of **Apache Airflow** to automate monitoring product profitability within a sales data mart. The primary goal is to identify products operating at a **negative net profit** and promptly notify the business team on a regular schedule to facilitate timely corrective actions.

This solution transforms manual, reactive reporting into an **automated, proactive alerting system**.

---

##  Technical Implementation

<img width="1894" height="1332" alt="image" src="https://github.com/user-attachments/assets/be8d602e-b685-48e4-acbe-9cbc525e4ed2" />

### Step 1: Creating the `Products_summary` View
A crucial step was establishing the analytical backbone of the project within the Sales Data Mart.

* **Purpose:** A single, consolidated SQL view was created to aggregate product sales data and calculate key financial metrics.
* **Key Metrics:** Total Sales, Freight, Cost of Goods Sold (COGS), Net Revenue, **Net Profit**, **Net Margin**, and a conditional `product_status_flag`.
* **Outcome:** This view consolidates all sales, freight, cost, and tax data per product, highlighting unprofitable items for focused business attention.
  



### Step 2: Extracting Data via Python
The Python component acts as the ETL bridge between the database and the reporting output.

* **Purpose:** A Python script connects to the SQL Server database, queries the `Products_summary` view, and extracts only the data corresponding to **risky products** ($\text{Net Profit} < 0$).
* **Output:** The extracted data is transformed and saved into a structured **CSV file**, ready to be attached to an alert email.



### Step 3: Automating with Apache Airflow
Apache Airflow orchestrates the end-to-end data pipeline.

* **Purpose:** The DAGs were created to fully automate the entire monitoring and alerting process without manual intervention.
* **Scheduling:** The DAG is configured to run automatically **every 10 days** using a custom CRON schedule.
* <img width="2306" height="887" alt="Screenshot 2025-10-16 173400" src="https://github.com/user-attachments/assets/c22f0781-fb17-4540-9f56-3e00a394e12d" />
![WhatsApp Image 2025-10-16 at 19 01 29_6f9b7bf2](https://github.com/user-attachments/assets/01fce3bf-3312-4842-b410-73a37bf63e49)

#### DAG Workflow Highlights

| Operator | Function |
| :--- | :--- |
| **`PythonOperator`** | Executes the Python script to connect to SQL Server, extract risky product data, and save it as a CSV file. |
| **`EmailOperator`** | Sends the generated CSV file as an attachment to the designated business team, along with a summary alert message. |
| **`BashOperator` (optional)** | Can be used for lightweight shell commands, such as data cleanup or triggering downstream systems. |

* **Containerization (Docker):** Deploying Airflow and its dependencies within containers for isolation and consistency.
* <img width="2160" height="1056" alt="Screenshot 2025-10-16 173831" src="https://github.com/user-attachments/assets/73893e30-73f9-474b-ae2c-61006c038604" />


#### Task 2
# ⚙️ Airflow: Initial DAG Setup

## Objective
To create and run a foundational Apache Airflow DAG demonstrating basic task dependencies and the use of the primary operators.

---

## 🛠️ Implementation Steps

### 1. DAG Definition
The DAG must be defined in Python within the `dags/` folder.

* **DAG Name:** `Airflow_Depi`

### 2. Task Definitions
Three sequential tasks were defined using different operators:

| Task ID | Operator | Functionality |
| :--- | :--- | :--- |
| **Task 1** | `BashOperator` | Prints the current system date (`bash_command='date'`) |
| **Task 2** | `PythonOperator` | Prints a personalized welcome message (`"Welcome to DEPI, Ali Ahmed!"`) |
| **Task 3** | `PythonOperator` | Generates a random number and persists it to a temporary file (`/tmp/random.txt`) |

### 3. Task Dependencies
The tasks are linked sequentially to enforce execution order.

* **Order:** Task 1 $\rightarrow$ Task 2 $\rightarrow$ Task 3

* <img width="2554" height="1226" alt="Screenshot 2025-10-16 143550" src="https://github.com/user-attachments/assets/518ba76a-70c2-44ec-8271-2ae7f6c55c9d" />
<img width="2543" height="782" alt="Screenshot 2025-10-16 144657" src="https://github.com/user-attachments/assets/a3a387bc-a21c-484a-9d84-a1da53b58d59" />
<img width="2559" height="597" alt="Screenshot 2025-10-16 144709" src="https://github.com/user-attachments/assets/22636f75-744e-44fb-b495-d3b0dee4b3a7" />
<img width="2559" height="706" alt="Screenshot 2025-10-16 144721" src="https://github.com/user-attachments/assets/932bc3f0-053b-4fec-a984-056b37044e2f" />
<img width="2559" height="785" alt="Screenshot 2025-10-16 144734" src="https://github.com/user-attachments/assets/1cc66171-7e29-46ad-8e10-c5b92a43f068" />








---

##  Benefits and Business Impact

### Step 4: Benefits
The automated pipeline delivers significant operational and strategic advantages.

* **Automates Reporting:** Eliminates the need for manual SQL queries and report generation, saving analyst time.
* **Proactive Alerts:** Provides a mechanism for timely and proactive alerts about **risky (loss-making) products**.
* **Improves Decision-Making:** Delivers timely, automated insights directly to decision-makers, facilitating quicker corrective actions (e.g., repricing, supplier negotiation, or discontinuation).

---

##  Skills and Experience Gained

### Step 5: Skills and Experience Gained
This project provided comprehensive, hands-on experience across the data engineering stack:

* **Airflow DAG Design:** Gained expertise in defining task dependencies, scheduling (CRON expressions), retry policies, and managing task context.
* **Operators:** Practical use of the `PythonOperator`, `BashOperator`, and the crucial `EmailOperator` for business notifications.
* **Airflow Concepts:** Deepened understanding of Airflow's architecture, including logging, task execution, and connection management.
* **SQL & Data Modeling:** Solidified skills in creating analytical views, performing complex metric aggregation (Net Profit/Margin), and designing profit indicators.
* **Python Integration:** Practical skills in connecting Python to SQL Server (e.g., using `pyodbc` or `sqlalchemy`), querying large datasets, and outputting structured CSV files.
* **Automation & Monitoring:** Built a complete, resilient end-to-end workflow to directly support business analysis and intervention.
