from unittest import TestCase
from app import app


Class CurrencyConverterTest(TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_index(self):
        with self.client:
            res = client.get('/')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('amount', html)

    def test_result_page(self):
        with self.client:
            res = client.get('/result')
            html = res.get_data(as_text=True)
            self.assertIn('$1', html)

