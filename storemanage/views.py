from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Currency
# Create your views here.
def currencyRegister(request):
    user = request.user
    if request.method == 'GET':
        return render(request,'storemanage/currency-form.html')
    data = request.POST
    currency = Currency(store=user,name=data['name'])
    currency.save()
    return redirect('index:index')
