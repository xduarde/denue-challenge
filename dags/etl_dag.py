from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator, BigQueryCreateEmptyDatasetOperator, BigQueryCreateEmptyTableOperator
from config.claves_entidades import claves
from config.tables import schemas
from datetime import datetime, date, timedelta
from process import extract_clean_data
from process import copy_data


default_args = {
    "owner": "airflow"
}

dag_init = DAG(
    "ingest_denue_data",
    description="Extract, clean and load DENUE data from INEGI API (monthly).",
    start_date=datetime(2022, 9, 27),
    default_args=default_args,
    tags=["Ingest", "DENUE", "INEGI"],
    schedule_interval="0 0 1 * *" # Cron to run once a month
    )


with dag_init as dag:
    date_str = date.today().strftime("%Y%m%d")
    delay = timedelta(seconds=30)

    connect = DummyOperator(task_id="relation")

    validate_staging_dataset = BigQueryCreateEmptyDatasetOperator(
                task_id="validate_staging_dataset",
                dataset_id="staging",
                exists_ok=True
            )

    validate_denue_dataset = BigQueryCreateEmptyDatasetOperator(
                task_id="validate_denue_dataset",
                dataset_id="inegi_denue",
                exists_ok=True
            )

    validate_staging_table = BigQueryCreateEmptyTableOperator(
            task_id="validate_staging_table",
            dataset_id=schemas["general_denue"]["dataset"],
            table_id="general_denue",
            schema_fields=schemas["general_denue"]["schema"],
            exists_ok=True
        )


    validate_staging_dataset.set_downstream(validate_denue_dataset)


    for id, state in claves.items():

        state = state.replace(" ", "_").lower()

        extract_task = PythonOperator(
            task_id=f"extract_{state}_data", 
            python_callable=extract_clean_data.main,
            op_kwargs={"id": id}
        )    


        copy_task = PythonOperator(
            task_id=f"copy_{state}", 
            python_callable=copy_data.main,
            op_kwargs={"id": id}
        )    


        validate_denue_dataset.set_downstream(extract_task)
        extract_task.set_downstream(validate_staging_table)
        validate_staging_table.set_downstream(copy_task)
        copy_task.set_downstream(connect)


    for table, value in schemas.items():

        if value["insert"]:
            validate_tables = BigQueryCreateEmptyTableOperator(
                task_id=f"validate_{table}_table",
                dataset_id=value["dataset"],
                table_id=table,
                schema_fields=value["schema"],
                exists_ok=True
            )

            insert_data = BigQueryInsertJobOperator(
                task_id=f"insert_{table}_data",
                configuration={
                    "query": {
                        "query": value["insert"],
                        "useLegacySql": False
                    }
                }
            )


            connect.set_downstream(validate_tables)
            validate_tables.set_downstream(insert_data)