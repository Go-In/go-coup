from django.contrib import admin

# Register your models here.
from storemanage.models.Currency import Currency
from storemanage.models.Ticket import Ticket

admin.site.register(Currency)
admin.site.register(Ticket)
