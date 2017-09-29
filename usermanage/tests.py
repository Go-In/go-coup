from django.test import TestCase
from django.contrib.auth.models import User

from . import models

class usermanageViewsTestCase(TestCase):
    def test_customer_register(self):
        resp = self.client.get('/user/register', follow = True)
        self.assertEqual(resp.status_code, 200)

    def test_store_register(self):
        resp = self.client.get('/user/store-register', follow = True)
        self.assertEqual(resp.status_code, 200)

    def test_customer_str(self):
        customer_user = User.objects.create_user('customer_username')
        customer = models.Customer(user = customer_user, first_name = 'customer_firstname')
        self.assertEqual(str(customer), customer.first_name)

    def test_store_title(self):
        store_user = User.objects.create_user('store_username')
        store = models.Store(user = store_user, store_name = 'store_storename' )
        self.assertEqual(str(store), store.store_name)
