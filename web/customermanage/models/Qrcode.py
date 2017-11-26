from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
# Create your models here.

class Qrcode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    qrcode = models.CharField(max_length=127)
    attribute = JSONField(default = dict())
