from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.forms import UserCreationForm
from customermanage.models import Coupon, Wallet
from storemanage.models import Ticket
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
# Create your views here.
from usermanage import models   

def customerRegister(request):
    if request.user.is_authenticated:
        return redirect('index:index')
    if request.method == 'GET':
        return render(request,'usermanage/register-customer.html')
    data = request.POST

    # check user already exits
    if User.objects.filter(username=data['username']).exists():
        return render(request, 'usermanage/register-customer.html', {
                'username_error' : True,
                })

    # check first name is too long
    if len(data['first_name']) > 30:
        return render(request, 'usermanage/register-customer.html', {
                'firstname_len_error' : True,
                })

    # check first name is too short
    if len(data['last_name']) > 30:
        return render(request, 'usermanage/register-customer.html', {
                'lastname_len_error' : True,
                })

    #check tel
    if len(data['tel']) > 12:
        return render(request, 'usermanage/register-customer.html', {
                'tel_len_error' : True,
                })

    # check password is too short
    if len(data['password']) < 8:
        return render(request, 'usermanage/register-customer.html', {
                'short_password_error' : True,
                })

    # check password is too long
    if len(data['password']) > 20:
        return render(request, 'usermanage/register-customer.html', {
                'long_password_error' : True,
                })   

    # check email
    try:
        validate_email(data['email'])
    except ValidationError as e:
        return render(request, 'usermanage/register-customer.html', {
                'email_error' : True,
                })
    else:
        return render(request, 'usermanage/register-customer.html', {
                'email_error' : False,
                })

    user = User.objects.create_user(username = data['username'], password = data['password'], email = data['email'])
    g = Group.objects.get(name='customer')
    g.user_set.add(user)
    user.save()
    g.save()
    customerprofile = models.Customer(user = user, first_name = data['first_name'], last_name = data['last_name'])
    customerprofile.save()
    return redirect('index:index')
