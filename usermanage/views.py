from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from . import views, models
def customerSignup(request):
    if request.user.is_authenticated:
        return redirect('index:index')
    if request.method == 'GET':
        return render(request,'usermanage/signup-customer.html')
    data = request.POST
    user = User.objects.create_user(data['username'], password = data['password'])
    g = Group.objects.get(name='customer')
    g.user_set.add(user)
    user.save()
    g.save()
    customerprofile = models.Customer(user = user)
    customerprofile.save()
    return redirect('index:index')

def storeSignup(request):
    if request.user.is_authenticated:
        return redirect('index:index')
    if request.method == 'GET':
        return render(request,'usermanage/signup-store.html')
    data = request.POST
    user = User.objects.create_user(data['username'], password = data['password'])
    g = Group.objects.get(name='store')
    g.user_set.add(user)
    user.save()
    g.save()
    storeprofile = models.Store(user = user, store_name=data['storename'])
    storeprofile.save()
    return redirect('index:index')

def signin(request):
    if request.user.is_authenticated:
        return redirect('index:index')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.GET.get("next") is not None:
                return HttpResponseRedirect(request.GET["next"])
            return redirect('index:index')
    return render(request,'usermanage/signin.html')

def signout(request):
    logout(request)
    return redirect('index:index')

@login_required()
def profile(request):
    user = request.user
    data = {'username':user.username,'email':user.email}
    if user.groups.filter(name='store').exists():
        store = models.Store.objects.get(user=user)
        data['store_name']=store.store_name
    elif user.groups.filter(name='customer').exists():
        customer = models.Customer.objects.get(user=user)
        data['first_name']=customer.first_name
        data['last_name']=customer.last_name
    print(data)
    return render(request,'usermanage/profile.html', context={'d':data})
