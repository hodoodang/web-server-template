# -*- coding: utf-8 -*-
import time
from random import randint
from typing import List
from concurrent.futures import ThreadPoolExecutor

from fastapi import FastAPI
from fastapi.testclient import TestClient


def get_urls(url: str, limit: int) -> List[str]:
    return [url + str(randint(1, limit)) for i in range(1, limit + 1)]


def test_sync_api_call(client: TestClient):
    sleep = 15
    urls = get_urls('/tests/sync?duration=', sleep)

    temp_res = client.get('/tests/sync/?duration=10')
    print(f'temp_res: {temp_res.json()}')

    start = time.time()

    with ThreadPoolExecutor(max_workers=10) as Pool:
        response = Pool.map(client.get, urls)

    print(f'time required {time.time() - start}')
    for res in response:
        print(res.json())

    return response


def test_async_api_call(client: TestClient):
    sleep = 15
    urls = get_urls('/tests/async?duration=', sleep)

    start = time.time()

    with ThreadPoolExecutor(max_workers=10) as Pool:
        response = Pool.map(client.get, urls)

    print(f'time required {time.time() - start}')
    for res in response:
        print(res.json())

    return response
