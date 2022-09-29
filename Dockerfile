FROM python:3.9-slim-bullseye

COPY requirements.txt .

RUN apt update \
    && apt install -y --no-install-recommends \
        build-essential \
        r-base \
        python3-dev \
        wait-for-it \
    && pip3 install --no-cache-dir -r requirements.txt \
    \
    # https://github.com/psycopg/psycopg2/issues/1360
    # required to build psycopg2 on arm (see below)
    && apt install -y --no-install-recommends \
        libpq-dev \
    && pip3 uninstall -y psycopg2-binary \
    && pip3 install --no-cache-dir psycopg2 \
    \
    && apt autoremove -y \
    && rm -rf /var/lib/apt/lists/* \
    && rm requirements.txt

ENV AIRFLOW_HOME="/opt/airflow"
WORKDIR ${AIRFLOW_HOME}
ENTRYPOINT [ "airflow" ]

ENV PYTHONPATH="${AIRFLOW_HOME}/dags:${PYTHONPATH}"

# no auth
RUN echo "AUTH_ROLE_PUBLIC = 'Admin'" >> "${AIRFLOW_HOME}/webserver_config.py"