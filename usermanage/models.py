from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    birthdate = models.DateField(null=True)
    tel = models.CharField(max_length=12, null=True)
    attribute = JSONField(default = dict)
    def __str__(self):
        return self.user

class Store(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=30)
    tel = models.CharField(max_length=12, null=True)
    attribute = JSONField(default = dict)

    def __str__(self):
        return self.user

class RightsSupport(models.Model):

    class Meta:
        managed = False
        permissions = (
            ('customer_rights', 'customer_rights'),
            ('store_rights', 'store_rights'),
        )
