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

def singin(request, error = ''):
    user = request.user
    if request.user.is_authenticated:
        return redirect_after_login(user)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.GET.get("next") is not None:
                return HttpResponseRedirect(request.GET["next"])
            return redirect_after_login(user)
        else:
             error = True
             return render(request, 'usermanage/login.html', {
             'error' : error
             })
    return render(request,'usermanage/login.html')
