import unittest
from app.app import app
import werkzeug

if not hasattr(werkzeug, '__version__'):
    werkzeug.__version__ = "mock-version"

class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
   
    def test_getItens(self):
        resposta = self.client.get('/items')
        self.assertEqual(resposta.status_code, 200)
        data = resposta.get_json()
        self.assertIn("item1", data["items"])
    
    def test_entrar(self):
        resposta_login = self.client.post('/login')
        self.assertEqual(resposta_login.status_code, 200)
        token = resposta_login.get_json()['access_token']
        resposta_protected = self.client.get('/protected',headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(resposta_protected.status_code, 200)
        self.assertIn("Protected route", resposta_protected.get_json()["message"])
    
    def test_swagger(self):
        resposta_swagger = self.client.get('/swagger/')
        self.assertEqual(resposta_swagger.status_code, 200)
        
if __name__ == '__main__':
    unittest.main()