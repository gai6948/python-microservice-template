import unittest

from fastapi.testclient import TestClient
from webapi.main import app


class TestGeneratingPair(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_pairs_generated_is_string_number_map(self):
        response = self.client.get("/v1/pairs")
        assert response.status_code == 200
        for key, value in response.json().items():
            assert type(key) == str
            assert type(value) == float
