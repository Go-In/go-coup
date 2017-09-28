from django.db import models
from storemanage.models import Currency
from django.contrib.auth.models import User

# Create your models here.
class Wallet(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=2)
