import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from application.initializer import IncludeAPIRouter


@pytest.fixture(scope="module")
def client():
    app = FastAPI()
    app.include_router(IncludeAPIRouter())
    client = TestClient(app)
    return client
