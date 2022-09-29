# denue-challenge

Project to extract, clean and ingest data from INEGI - Directorio Estadístico Nacional de Unidades Económicas (DENUE) to BigQuery (monthly). Data pipeline developed in Python, orchestrated in Airflow and implemented in Docker.


## Getting Started

### Installation

Clone the repository.

```bash
git clone https://github.com/xduarde/denue-challenge.git
```
```bash
cd denue-challenge
```


## Usage

The data pipeline is deployed from a [Docker](https://docs.docker.com/get-docker/) container, through an [Airflow image](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html). Moreover, the INEGI - DENUE data model is built and desinged in a data warehouse (BigQuery). 

The follow command deploys the environment and initialize the pipeline:

```bash
docker compose up --build
```

1. **Deploy the Airflow container** 
2. **Configure GCP (BigQuery) connection** 
3. **Trigger the ingest_denue_data Dag** 
    - Validate datasets.
    - Extract data from INEGI API by state.
    - Clean data.
    - Validate tables.
    - Insert data to staging table.
    - Execute queries to populate model.

In order to monitor the ingest_denue_data, access the Airflow Web Server in:

> **[http://localhost:8080/](http://localhost:8080/)** 

**Extras:**
- BigQuery [Dataplex](https://cloud.google.com/dataplex/docs/check-data-quality) tool to create and execute data qualiy tasks.
- BigQuery BI Engine to create a [relation to Data Studio](https://cloud.google.com/bigquery/docs/bi-engine-data-studio?hl=en).
- Data Studio to exploit data.


## Data Model

![alt text](/img/denue-model.png.png)


## License

Distributed under the MIT License. See LICENSE for more information.