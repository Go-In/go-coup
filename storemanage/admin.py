from django.contrib import admin

# Register your models here.
from .models import Currency, Ticket

admin.site.register(Currency)
admin.site.register(Ticket)
