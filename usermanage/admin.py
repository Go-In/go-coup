from django.contrib import admin

# Register your models here.
from .models import Customer, Store

admin.site.register(Customer)
admin.site.register(Store)
