import unittest

from fastapi.testclient import TestClient
from webapi.main import app


class TestGenerateFibonacciNumber(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_fibonacci_10_is_correct(self):
        response = self.client.get("/v1/fib?n=10")
        assert response.status_code == 200
        assert response.json()["value"] == 89

    def test_fibonacci_251_rejected(self):
        response = self.client.get("/v1/fib?n=251")
        assert response.status_code == 400
