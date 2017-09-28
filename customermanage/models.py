from django.db import models
from storemanage.models import Currency, Ticket
from django.contrib.auth.models import User

# Create your models here.
class Wallet(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=2)

class Coupon(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    remaining_date = models.DateTimeField(null=True)
    active = models.BooleanField(default=True)
