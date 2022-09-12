# -*- coding: utf-8 -*-
import os
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.main import create_app


@pytest.fixture(scope="session")
def app():
    os.environ["API_ENV"] = "test"
    return create_app()


@pytest.fixture(scope="session")
def client(app):
    return TestClient(app)


@pytest.fixture(scope="session")
def filepath_or_buffer():
    project_path = str(Path(__file__).parent.parent)
    filepath = [project_path, 'data', 'sample.json']
    return os.path.join(*filepath)


@pytest.fixture(scope="session")
def big_filepath_or_buffer():
    project_path = str(Path(__file__).parent.parent)
    filepath = [project_path, 'data', 'big_data.json']
    return os.path.join(*filepath)
