from django.test import TestCase
from django.contrib.auth.models import User

from . import models

class usermanageViewsTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('testing_user', password = 'testing_password')

    def test_customer_register_view(self):
        resp = self.client.get('/user/register', follow = True)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.templates[0].name, 'usermanage/register-customer.html')

    def test_store_register_view(self):
        resp = self.client.get('/user/store-register', follow = True)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.templates[0].name, 'usermanage/register-store.html')

    def test_user_login_view(self):
        resp = self.client.get('/user/login', follow = True)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.templates[0].name, 'usermanage/login.html')

    def test_user_logout_view(self):
        resp = self.client.get('/user/logout', follow = True)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.templates[0].name, 'index/index.html')

    def test_not_loged_user_profile_view(self):
        resp = self.client.get('/user/profile', follow = True)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.templates[0].name, 'usermanage/login.html')

    def test_loged_user_profile_view(self):
        resp = self.client.login(username = 'testing_user', password = 'testing_password')
        resp = self.client.get('/user/profile', follow = True)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.templates[0].name, 'usermanage/profile.html')

class usermanageFunctionTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('testing_user', password = 'testing_password')

    def test_loged_user_not_be_able_to_login_again(self):
        resp = self.client.login(username = 'testing_user', password = 'testing_password')
        resp = self.client.get('/user/login', follow = True)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.templates[0].name, 'index/index.html')

    def test_user_logout(self):
        resp = self.client.login(username = 'testing_user', password = 'testing_password')
        resp = self.client.get('/user/login', follow = True)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.templates[0].name, 'index/index.html')
        
        resp = self.client.get('/user/logout', follow = True)
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get('/user/login', follow = True)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.templates[0].name, 'usermanage/login.html')

    def test_customer_str(self):
        customer_user = User.objects.create_user('customer_username')
        customer = models.Customer(user = customer_user, first_name = 'customer_firstname')
        self.assertEqual(str(customer), customer.first_name)

    def test_store_str(self):
        store_user = User.objects.create_user('store_username')
        store = models.Store(user = store_user, store_name = 'store_storename' )
        self.assertEqual(str(store), store.store_name)
