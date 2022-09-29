import os
from airflow.providers.google.cloud.hooks.bigquery import BigQueryHook
from google.cloud import bigquery

def main(id):
    hook = BigQueryHook()

    client = bigquery.Client(project=hook._get_field("project"), credentials=hook._get_credentials())

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV, field_delimiter=";", autodetect=False
    )

    table_id = "bamboo-theorem-363821.staging.general_denue"

    with open(f"{os.getcwd()}/{id}.csv", "rb") as source_file:
        job = client.load_table_from_file(source_file, table_id, job_config=job_config)

    job.result()  # Waits for the job to complete.

    table = client.get_table(table_id)  # Make an API request.
    
    print(
        "Loaded {} rows and {} columns to {}".format(
            table.num_rows, len(table.schema), table_id
        )
    )
    