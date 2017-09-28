from django.test import TestCase

class usermanageViewsTestCase(TestCase):
    def test_user_signup(self):
        resp = self.client.get('/user/signup', follow = True)
        self.assertEqual(resp.status_code, 200)

    def test_store_signup(self):
        resp = self.client.get('/user/store-signup', follow = True)
        self.assertEqual(resp.status_code, 200)
