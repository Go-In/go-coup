from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from . import views, models
def customerSignup(request):
    if request.user.is_authenticated:
        return redirect('index:index')
    if request.method == 'GET':
        return render(request,'usermanage/signup-customer.html')
    data = request.POST

    # check user already exits
    if User.objects.filter(username=data['username']).exists():
        return render(request,'usermanage/signup-customer.html')

    user = User.objects.create_user(data['username'], password = data['password'], email = data['email'])
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

     # check user already exits
    if User.objects.filter(username=data['username']).exists():
        return render(request,'usermanage/signup-store.html')

    user = User.objects.create_user(data['username'], password = data['password'])
    g = Group.objects.get(name='store')
    g.user_set.add(user)
    user.save()
    g.save()
    storeprofile = models.Store(user = user, store_name=data['storename'])
    storeprofile.save()
    return redirect_after_signin(user)

def signin(request):
    user = request.user
    if request.user.is_authenticated:
        return redirect_after_signin(user)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.GET.get("next") is not None:
                return HttpResponseRedirect(request.GET["next"])
            return redirect_after_signin(user)
    return render(request,'usermanage/signin.html')

def redirect_after_signin(user):
    if user.groups.filter(name='store').exists():
        print('store')
        return redirect('store:index')
    else:
        print('user')
        return redirect('index:index')

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
    return render(request,'usermanage/profile.html', context={'d':data})


def isStore(user):
    return user.groups.filter(name='store').exists()

def isCustomer(user):
    return user.groups.filter(name='customer').exists()

@permission_required('usermanage.customer_rights',raise_exception=True)
def customertest(request):
    return render(request,'usermanage/customertest.html')

@permission_required('usermanage.store_rights',raise_exception=True)
def storetest(request):
    return render(request,'usermanage/storetest.html')

def userProfileContextGenerate(user):
    data = {'username':user.username,'email':user.email}
    if user.groups.filter(name='store').exists():
        store = models.Store.objects.get(user=user)
        data['store_name']=store.store_name
    elif user.groups.filter(name='customer').exists():
        customer = models.Customer.objects.get(user=user)
        data['first_name']=customer.first_name
        data['last_name']=customer.last_name
        data['birthdate']=customer.birthdate.strftime('%Y-%m-%d') if customer.birthdate is not None else None
    return {k:v for k,v in data.items() if v is not None}

@login_required()
@permission_required('usermanage.customer_rights',raise_exception=True)
def customerProfile(request):
    data = {'data':userProfileContextGenerate(request.user)}
    return render(request,'index/profile.html',data)

@login_required()
@permission_required('usermanage.customer_rights',raise_exception=True)
def customerSetting(request):
    if request.method == 'GET':
        data = {'data':userProfileContextGenerate(request.user)}
        return render(request,'index/setting.html',data)

    user = request.user
    data = request.POST
    customer_attrib = {k:v for k,v in data.items()}
    customer_attrib.pop('csrfmiddlewaretoken', None)
    customer = models.Customer.objects.get(user=user)
    print(customer_attrib)
    for k,v in customer_attrib.items():
        setattr(customer,k,v)
    customer.save()
    user.email = customer_attrib['email']
    user.save()
    return render(request,'index/setting.html',{'data':customer_attrib})
