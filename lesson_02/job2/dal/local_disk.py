from typing import List, Dict, Any
import os
import json
import shutil
import fastavro


# RAW_DIR = os.path.join(os.environ.get('BASE_DIR'), 'raw', 'sales', '2022-08-09')
# STAGE_DIR = os.path.join(os.environ.get('BASE_DIR'), 'stg', 'sales', '2022-08-09')

def _get_avro_schema():
    return {
        "type": "record",
        "name": "MyRecord",
        "fields":  [
            {"name": "client", "type": "string"},
            {"name": "purchase_date", "type": "string"},
            {"name": "product", "type": "string"},
            {"name": "price", "type": "int"}
        ]
    }


def _load_json_data(path: str):
    with open(path, "r") as json_file:
        return json.load(json_file)


def write_to_avro(raw_dir:str, stg_dir:str) -> None:
    # clean up the folder before writing the new batch
    shutil.rmtree(stg_dir, ignore_errors=True)
    # create folder if does not exist
    os.makedirs(stg_dir, exist_ok=True)

    # getting file name that needed to be converted
    sub_folder_name = raw_dir.split("\\")[-1]
    file_name = f"sales_{sub_folder_name}"

    avro_path = os.path.join(stg_dir, f'{file_name}.avro')
    json_path = os.path.join(raw_dir, f'{file_name}.json')
    with open(avro_path, 'wb') as avro_file:
        fastavro.writer(avro_file, _get_avro_schema(), _load_json_data(json_path))
