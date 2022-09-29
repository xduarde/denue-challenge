schemas = {
    "general_denue": {
        "dataset": "staging",
        "insert": "",
        "schema": [{"name":  "clee", "type": "STRING", "mode": "REQUIRED"},
                    {"name": "id", "type": "INTEGER", "mode": "REQUIRED"},
                    {"name": "nombre", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "razon_social", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "clase_actividad", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "estrato", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "tipo_vialidad", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "calle", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "num_exterior", "type": "INTEGER", "mode": "NULLABLE"},
                    {"name": "num_interior", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "colonia", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "cp", "type": "INTEGER", "mode": "NULLABLE"},
                    {"name": "ubicacion", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "telefono", "type": "INTEGER", "mode": "NULLABLE"},
                    {"name": "correo_e", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "sitio_internet", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "tipo", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "longitud", "type": "FLOAT64", "mode": "NULLABLE"},
                    {"name": "latitud", "type": "FLOAT64", "mode": "NULLABLE"},
                    {"name": "tipo_corredor_industrial", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "nom_corredor_industrial", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "numero_local", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "localidad", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "municipio", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "entidad", "type": "STRING", "mode": "NULLABLE"}]
    },
    "establecimientos": {
        "dataset": "inegi_denue",
        "insert": """INSERT INTO `bamboo-theorem-363821.inegi_denue.establecimientos` (clee, id, nombre, telefono, tipo, correo_e, sitio_internet)
                        SELECT
                        clee, 
                        id, 
                        nombre, 
                        telefono, 
                        tipo, 
                        correo_e, 
                        sitio_internet
                        FROM `bamboo-theorem-363821.staging.general_denue`;""",
        "schema": [{"name":  "clee", "type": "STRING", "mode": "REQUIRED"},
                    {"name": "id", "type": "INTEGER", "mode": "REQUIRED"},
                    {"name": "nombre", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "telefono", "type": "INTEGER", "mode": "NULLABLE"},
                    {"name": "tipo", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "correo_e", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "sitio_internet", "type": "STRING", "mode": "NULLABLE"}]
    },
    "ubicacion": {
        "dataset": "inegi_denue",
        "insert": """INSERT INTO `bamboo-theorem-363821.inegi_denue.ubicacion` (clee, id, entidad, municipio, localidad, colonia, calle,tipo_vialidad, num_exterior, num_interior, numero_local, cp, longitud, latitud)
                        SELECT
                        clee, id, entidad, municipio, localidad, colonia, calle,tipo_vialidad, num_exterior, num_interior, numero_local, cp, longitud, latitud
                        FROM `bamboo-theorem-363821.staging.general_denue`;""",
        "schema": [{"name":  "clee", "type": "STRING", "mode": "REQUIRED"},
                    {"name": "id", "type": "INTEGER", "mode": "REQUIRED"},
                    {"name": "entidad", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "municipio", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "localidad", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "colonia", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "calle", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "tipo_vialidad", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "num_exterior", "type": "INTEGER", "mode": "NULLABLE"},
                    {"name": "num_interior", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "numero_local", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "cp", "type": "INTEGER", "mode": "NULLABLE"},
                    {"name": "longitud", "type": "FLOAT64", "mode": "NULLABLE"},
                    {"name": "latitud", "type": "FLOAT64", "mode": "NULLABLE"}]
    },
    "actividad_economica": {
        "dataset": "inegi_denue",
        "insert": """INSERT INTO `bamboo-theorem-363821.inegi_denue.actividad_economica` (clee, id, razon_social, clase_actividad, estrato, tipo_corredor_industrial, nom_corredor_industrial)
                        SELECT
                        clee, id, razon_social, clase_actividad, estrato, tipo_corredor_industrial, nom_corredor_industrial
                        FROM `bamboo-theorem-363821.staging.general_denue`;""",
        "schema": [{"name":  "clee", "type": "STRING", "mode": "REQUIRED"},
                    {"name": "id", "type": "INTEGER", "mode": "REQUIRED"},
                    {"name": "razon_social", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "clase_actividad", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "estrato", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "tipo_corredor_industrial", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "nom_corredor_industrial", "type": "STRING", "mode": "NULLABLE"}]
    }                
}