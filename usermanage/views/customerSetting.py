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
def customerSetting(request):
    if request.method == 'GET':
        data = {'data':userProfileContextGenerate(request.user)}
        return render(request,'index/setting.html',data)

    user = request.user
    data = request.POST
    customer_attrib = {k:v for k,v in data.items() if v != ''}
    customer_attrib.pop('csrfmiddlewaretoken', None)
    customer = models.Customer.objects.get(user=user)
    for k,v in customer_attrib.items():
        setattr(customer,k,v)
    customer.save()
    if 'email' in customer_attrib:
        user.email = customer_attrib['email']
    user.save()
    return render(request,'index/setting.html',{'data':customer_attrib})
