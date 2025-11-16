import unittest

from fastapi.testclient import TestClient

from main import app


class TestFastAPIApp(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)

    def tearDown(self) -> None:
        self.client.close()

    def test_health_endpoint_returns_ok(self) -> None:
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})

    def test_average_endpoint_returns_result(self) -> None:
        response = self.client.post("/average", json={"values": [1, 2, 3, 4]})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"average": 2.5})

    def test_average_endpoint_rejects_empty_values(self) -> None:
        response = self.client.post("/average", json={"values": []})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["detail"], "values must contain at least one number")


if __name__ == "__main__":
    unittest.main()
