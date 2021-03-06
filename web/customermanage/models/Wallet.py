from django.db import models
from storemanage.models.Currency import Currency
from storemanage.models.Ticket import Ticket
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
# Create your models here.
class Wallet(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)
    attribute = JSONField(default = dict())
