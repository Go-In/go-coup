from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from . import views, models
def customerSignup(request):
    if request.method == 'GET':
        return render(request,'usermanage/signup-customer.html')
    data = request.POST
    user = User.objects.create_user(data['username'], password = data['password'])
    user.save()
    customerprofile = models.Customer(user = user)
    customerprofile.save()
    return redirect('index:index')

def storeSignup(request):
    if request.method == 'GET':
        return render(request,'usermanage/signup-store.html')
    data = request.POST
    user = User.objects.create_user(data['username'], password = data['password'])
    user.save()
    storeprofile = models.Store(user = user, store_name=data['storename'])
    storeprofile.save()
    return redirect('index:index')
