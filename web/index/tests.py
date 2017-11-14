from django.test import TestCase

class indexViewsTestCase(TestCase):
    def test_index_view(self):
        resp = self.client.get('/', follow = True)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.templates[0].name, 'index/index.html')

    def test_cart_view_with_no_cart(self):
        resp = self.client.get('/cart', follow = True)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.templates[0].name, 'index/index.html')

    def test_cart_view_with_empty_cart(self):
        resp = self.client.get('/cart/?cart=', follow = True)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.templates[0].name, 'index/cart.html')
