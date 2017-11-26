from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.forms import UserCreationForm
from customermanage.models import Coupon, Wallet
from storemanage.models import Ticket
# Create your views here.
from usermanage import models


def userProfileContextGenerate(user):
    data = {'username':user.username,'email':user.email,'first_name':user.first_name}
    if user.groups.filter(name='store').exists():
        store = models.Store.objects.get(user=user)
        data['store_name']=store.store_name
    elif user.groups.filter(name='customer').exists():
        customer = models.Customer.objects.get(user=user)
        data['first_name']=customer.first_name
        data['last_name']=customer.last_name
        data['birthdate']=customer.birthdate.strftime('%Y-%m-%d') if customer.birthdate is not None else None
    return {k:v for k,v in data.items() if v is not None}
