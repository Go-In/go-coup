from django.test import TestCase

class indexViewsTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/', follow = True)
        self.assertEqual(resp.status_code, 200)
