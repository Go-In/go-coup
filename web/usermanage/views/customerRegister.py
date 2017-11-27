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
from .validateForm import validateCustomerForm
from .redirect_after_login import redirect_after_login

def customerRegister(request):
    if request.user.is_authenticated:
        return redirect('index:index')
    if request.method == 'GET':
        return render(request,'usermanage/register-customer.html')

    data = request.POST

    error = validateCustomerForm(data)

    if error:
        return render(request,'usermanage/register-customer.html', {
            'error' : error
        })

    user = User.objects.create_user(username = data['username'], password = data['password'], email = data['email'])
    g = Group.objects.get(name='customer')
    g.user_set.add(user)
    user.save()
    g.save()
    customerprofile = models.Customer(user = user, first_name = data['first_name'], last_name = data['last_name'])
    customerprofile.save()
    user = authenticate(request,username = data['username'], password=data['password'])
    login(request, user)

    return redirect_after_login(user)
