from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

# Create your models here.

class RightsSupport(models.Model):

    class Meta:
        managed = False
        permissions = (
            ('customer_rights', 'customer_rights'),
            ('store_rights', 'store_rights'),
        )
