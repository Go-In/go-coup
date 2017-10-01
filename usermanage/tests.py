from django.test import TestCase
from django.contrib.auth.models import User, Group, Permission

from . import models

class usermanageViewsTestCase(TestCase):

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


class customerViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testing_user', password = 'testing_password')
        self.group = Group.objects.create(name = 'customer')
        self.userProfile = models.Customer(user = self.user)


        customer_rights = Permission.objects.get(name = 'customer_rights')

        self.group.permissions.add(customer_rights)
        self.group.user_set.add(self.user)

        self.user.save()
        self.group.save()
        self.userProfile.save()

    def tearDown(self):
        self.user.delete()
        self.group.delete()
        self.userProfile.delete()

    def test_loged_customer_profile_view(self):
        resp = self.client.login(username = 'testing_user', password = 'testing_password')
        resp = self.client.get('/user/profile', follow = True)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.templates[0].name, 'index/profile.html')

class storeViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testing_user', password = 'testing_password')
        self.group = Group.objects.create(name = 'store')
        self.userProfile = models.Store(user = self.user)


        store_rights = Permission.objects.get(name = 'store_rights')

        self.group.permissions.add(store_rights)
        self.group.user_set.add(self.user)

        self.user.save()
        self.group.save()
        self.userProfile.save()

    def tearDown(self):
        self.user.delete()
        self.group.delete()
        self.userProfile.delete()

    def test_loged_store_profile_view(self):
        resp = self.client.login(username = 'testing_user', password = 'testing_password')
        resp = self.client.get('/user/profile', follow = True)
        self.assertEqual(resp.status_code, 403)

class usermanageFunctionTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testing_user', password = 'testing_password')

        self.user.save()

    def tearDown(self):
        self.user.delete()

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
