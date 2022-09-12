import os
import json
from pathlib import Path

import ijson
import pandas as pd
import dask.dataframe as dd


def read_json(filepath_or_buffer):
    with open(filepath_or_buffer, 'r', encoding='utf-8') as file:
        json_data = file.readlines()
    data = [json.loads(line) for line in json_data]
    return data


def read_json_by_ijson(filepath_or_buffer):
    with open(filepath_or_buffer, 'rb', encoding='utf-8') as file:
        ijson_data = ijson.items(file)
    return ijson_data


def read_json_by_pandas(filepath_or_buffer):
    return pd.read_json(filepath_or_buffer, encoding='utf-8', lines=True)


def read_json_by_dask(filepath_or_buffer):
    return dd.read_json(filepath_or_buffer, encoding='utf-8', lines=True)


if __name__ == '__main__':
    base_path = str(Path(__file__).parent.parent.parent)
    filepath = base_path + '/data/sample.json'
    path = ['data', 'sample.json']
    path = os.path.join(*path)
    print(os.path.join(base_path, path))

    print(filepath)
    df = read_json_by_dask(filepath)
    print(df.count().compute().to_string())
    # a = dd.DataFrame()
