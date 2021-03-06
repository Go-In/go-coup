from django.db import models
from storemanage.models.Currency import Currency
from storemanage.models.Ticket import Ticket
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
# Create your models here.

class Coupon(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    remaining_date = models.DateTimeField(null=True)
    active = models.BooleanField(default=True)
    attribute = JSONField(default = dict())
