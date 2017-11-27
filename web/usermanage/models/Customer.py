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
    attribute = JSONField(default = dict())
    profile_image_url = models.CharField(max_length=1023, null=True)
    available = models.BooleanField(default=True)
    # endpoint = models.CharField(max_length=1000, null=True)
    # keys = model.CharField(max_length=1000)

    def __str__(self):
        return self.first_name
