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
from .redirect_after_login import redirect_after_login

def storeRegister(request):
    if request.user.is_authenticated:
        return redirect('index:index')
    if request.method == 'GET':
        return render(request,'usermanage/register-store.html')
    data = request.POST

     # check user already exists
    if User.objects.filter(username=data['username']).exists():
        return render(request,'usermanage/register-store.html', {
        'user_error' : True,
        })
    
    # check storename already exists
    if models.Store.objects.filter(store_name=data['storename']).exists():
        return render(request,'usermanage/register-store.html', {
        'store_error' : True,
        })

    #check username out of range

    if len(data['username']) > 30:
        return render(request, 'usermanage/register-store.html', {
            'user_len' : True,
        })
    
    #check storename out of range

    if len(data['storename']) > 30:
        return render(request, 'usermanage/register-store.html', {
            'store_len' : True,
        })

    user = User.objects.create_user(data['username'], password = data['password'])
    g = Group.objects.get(name='store')
    g.user_set.add(user)
    user.save()
    g.save()
    storeprofile = models.Store(user = user, store_name=data['storename'], profile_image_url=data['profile_image_url'])
    storeprofile.save()
    return redirect_after_login(user)
