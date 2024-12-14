import unittest
from app import create_app

class FlaskAPITestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_health_check(self):
        response = self.client.get('/api/health')
        self.assertEqual(response.status_code, 200)
        self.assertIn('healthy', response.get_json()['status'])

    def test_hello_world(self):
        response = self.client.get('/api/test')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello, World!', response.get_json()['message'])

    def test_process_text(self):
        response = self.client.post('/api/text', json={"text": "test"})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Received your text!', response.get_json()['message'])

    def test_invalid_data_validation(self):
        response = self.client.post('/api/validate', json={"name": "John"})
        self.assertEqual(response.status_code, 400)
        self.assertIn('errors', response.get_json())

if __name__ == '__main__':
    unittest.main()

