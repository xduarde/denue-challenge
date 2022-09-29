import os
import requests
import numpy as np
import pandas as pd
from config.data_types import data_types 


def extract(api_response):
    df = pd.DataFrame(api_response)
    return df

def clean(df):
    df.columns = df.columns.str.lower()
    df.telefono = df.telefono.str.replace(r"\D+", "", regex=True) #clean non-numerical values
    df.estrato = df.estrato.str.replace(" a ", "-").str.replace(" personas", "").str.replace(" y más", "+")
    df.correo_e = df.correo_e.str.lower()
    df.sitio_internet = df.sitio_internet.str.lower()
    df[['localidad', 'municipio', 'entidad']] = df.ubicacion.str.split(",", n=2, expand=True) #expand column to get localidad, municipio, entidad
    df = df.apply(lambda x: x.str.strip()).replace("", np.nan)

    for col, data_type in data_types.items():
        if "int" in data_type:
            df[col] = df[col].astype("float").astype("Int64")
        else:
            df[col] = df[col].astype(dtype=data_type)

    object_cols = df.select_dtypes("object").columns
    df[object_cols] = df[object_cols].replace("nan", "")
    
    return df


def main(id):
    url = f"https://www.inegi.org.mx/app/api/denue/v1/consulta/BuscarEntidad/todos/{id}/1/999999999999/0e21577e-b1f0-422f-83ab-0f0a93c994cf"

    #DENUE API request
    response = requests.get(url).json()

    df = extract(response)

    cleaned_df = clean(df)

    cleaned_df.to_csv(f"{os.getcwd()}/{id}.csv", index=False, header=False, sep=";", encoding="utf-8")