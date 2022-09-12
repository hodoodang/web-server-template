import time

from app.utils import read_json, read_json_by_dask, read_json_by_pandas


def test_read_json(filepath_or_buffer):
    start_time = time.time()
    data = read_json(filepath_or_buffer)
    load_time = time.time() - start_time

    assert type(data[0]) == dict
    assert len(data) == 10000
    assert load_time <= 0.2
