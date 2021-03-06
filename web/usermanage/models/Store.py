from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

# Create your models here.

class Store(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=30)
    tel = models.CharField(max_length=12, null=True)
    attribute = JSONField(default = dict())
    profile_image_url = models.CharField(max_length=1023, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.store_name
