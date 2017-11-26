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

@login_required()
def profile(request):
    user = request.user
    data = {'username':user.username,'email':user.email, 'firstname':user.first_name, 'lastname':user.last_name}
    if user.groups.filter(name='store').exists():
        store = models.Store.objects.get(user=user)
        data['store_name']=store.store_name
    elif user.groups.filter(name='customer').exists():
        customer = models.Customer.objects.get(user=user)
        data['first_name']=customer.first_name
        data['last_name']=customer.last_name
    return render(request,'usermanage/profile.html', context={'d':data})
