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
from .validateForm import validateStoreForm

def storeRegister(request):
    if request.user.is_authenticated:
        return redirect('index:index')
    if request.method == 'GET':
        return render(request,'usermanage/register-store.html')
    data = request.POST

    error = validateStoreForm(data)
    
    if error:
        return render(request, 'usermanage/register-store.html', {
            'error' : error
        })
    

    user = User.objects.create_user(data['username'], password = data['password'])
    g = Group.objects.get(name='store')
    g.user_set.add(user)
    user.save()
    g.save()
    storeprofile = models.Store(user = user, store_name=data['storename'], profile_image_url=data['profile_image_url'])
    storeprofile.save()
    return redirect_after_login(user)

