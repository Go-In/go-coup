from django.test import TestCase
from django.contrib.auth.models import User, Group, Permission

from usermanage import models

class storemanageViewsTestCase(TestCase):
    def test_not_loged_user_currency_add_view(self):
        resp = self.client.get('/store/currency/add', follow = True)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.templates[0].name, 'usermanage/login.html')

    def test_not_loged_user_ticket_add_view(self):
        resp = self.client.get('/store/add', follow = True)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.templates[0].name, 'usermanage/login.html')

class customerStoremanageViewsTestCase(TestCase):
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

    def test_loged_customer_currency_add_view(self):
        resp = self.client.login(username = 'testing_user', password = 'testing_password')
        resp = self.client.get('/store/currency/add', follow = True)
        self.assertEqual(resp.status_code, 403)

    def test_loged_customer_ticket_add_view(self):
        resp = self.client.login(username = 'testing_user', password = 'testing_password')
        resp = self.client.get('/store/add', follow = True)
        self.assertEqual(resp.status_code, 403)

class storeStoremanageViewsTestCase(TestCase):
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

    def test_loged_store_currency_add_view(self):
        resp = self.client.login(username = 'testing_user', password = 'testing_password')
        resp = self.client.get('/store/currency/add', follow = True)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.templates[0].name, 'storemanage/currency-form.html')

    def test_loged_store_ticket_add_view(self):
        resp = self.client.login(username = 'testing_user', password = 'testing_password')
        resp = self.client.get('/store/add', follow = True)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.templates[0].name, 'store/add.html')
