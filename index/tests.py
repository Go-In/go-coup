from django.test import TestCase

class indexViewsTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/', follow = True)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.templates[0].name, 'index/index.html')

    def test_cart(self):
        resp = self.client.get('/cart', follow = True)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.templates[0].name, 'index/cart.html')
