from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    def __str__(self):
        return self.user

class Store(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=30)
    def __str__(self):
        return self.user

class RightsSupport(models.Model):

    class Meta:

        managed = False  # No database table creation or deletion operations \
                         # will be performed for this model.

        permissions = (
            ('customer_rigths', 'Global customer rights'),
            ('store_rights', 'Global store rights'), 
            ('any_rights', 'Global any rights'),
        )
