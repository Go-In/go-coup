from django.contrib import admin

# Register your models here.
from usermanage.models.Customer import Customer
from usermanage.models.Store import Store

admin.site.register(Customer)
admin.site.register(Store)
