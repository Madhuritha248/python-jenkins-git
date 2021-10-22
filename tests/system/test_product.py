import json
from unittest import TestCase
from myPage1 import app

class ProductTest(TestCase):
    def test_welcome(self):
        with app.test_client() as c:
            resp = c.get('/api/products')
            self.assertEqual(resp.status_code,200)
            self.assertEqual(json.loads(resp.get_data()),
                             [
                                 {
                                     "pid": 1,
                                     "pname": "oneplus",
                                     "price": 189900,
                                     "rating": 4.8

                                 },
                                 {
                                     "pid": 4,
                                     "pname": "samsungflip",
                                     "price": 149999.5,
                                     "rating": 3.6

                                 },
                                 {
                                     "pid": 6,
                                     "pname": "realmeNarzo",
                                     "price": 30000,
                                     "rating": 4.8

                                 }]
                             )