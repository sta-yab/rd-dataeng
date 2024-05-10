from typing import List, Dict, Any
import os
import json
import shutil


def save_to_disk(json_content: List[Dict[str, Any]], path: str) -> None:
    # clean up the folder before writing the new batch
    shutil.rmtree(path, ignore_errors=True)
    # create folder if does not exist
    os.makedirs(path, exist_ok=True)

    path_with_file = os.path.join(path, f'sales_{json_content[0]["purchase_date"]}.json')
    with open(path_with_file, "w") as json_file:
        json.dump(json_content, json_file)
