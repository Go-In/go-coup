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
from . import userProfileContextGenerate

@login_required()
@permission_required('usermanage.customer_rights',raise_exception=True)
def customerProfile(request):
    data = {'data':userProfileContextGenerate(request.user)}
    return render(request,'index/profile.html',data)
