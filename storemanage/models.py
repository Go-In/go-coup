from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

# Create your models here.

class Currency(models.Model):
    name = models.CharField(max_length=30)
    store = models.ForeignKey(User, on_delete=models.CASCADE)
    attribute = JSONField(default = dict())
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    name = models.CharField(max_length=127)
    price = models.PositiveIntegerField()
    detail = models.TextField(max_length=1023)
    expire_date = models.DateField() #วันหมดอายุของคูปอง
    is_period = models.BooleanField()
    remaining_day = models.PositiveIntegerField(null=True) #จำนวนวันที่คูปองสามารถใช้งานได้ นับตั้งแต่การซื้อ
    is_limit = models.BooleanField()
    remain = models.IntegerField(null=True)  #จำนวนที่ยังเหลืออยู่
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    store = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket_image_url = models.CharField(max_length=1023, null=True)
    content_image_url = models.CharField(max_length=1023, null=True)
    attribute = JSONField(default = dict())
    available = models.BooleanField(default=True)
