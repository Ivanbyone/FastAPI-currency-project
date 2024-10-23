""" """

from fastapi.testclient import TestClient

from src.factory.app import create_application

test_client: TestClient = TestClient(app=create_application())
