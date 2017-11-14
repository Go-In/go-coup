from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

# Create your models here.

class Currency(models.Model):
    name = models.CharField(max_length=30)
    store = models.ForeignKey(User, on_delete=models.CASCADE)
    attribute = JSONField(default=dict())
    available = models.BooleanField(default=True)
    stat = JSONField(default=dict())
    raw_stat = JSONField(default=dict())

    def __str__(self):
        return self.name
