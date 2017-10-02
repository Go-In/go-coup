from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.forms import UserCreationForm
from customermanage.models import Coupon, Wallet
from storemanage.models import Ticket
# Create your views here.
from . import views, models
def customerRegister(request):
    if request.user.is_authenticated:
        return redirect('index:index')
    if request.method == 'GET':
        return render(request,'usermanage/register-customer.html')
    data = request.POST

    # check user already exits
    if User.objects.filter(username=data['username']).exists():
        return render(request, 'usermanage/register-customer.html', {
                'error' : True,
                })

    user = User.objects.create_user(username = data['username'], password = data['password'], email = data['email'])
    g = Group.objects.get(name='customer')
    g.user_set.add(user)
    user.save()
    g.save()
    customerprofile = models.Customer(user = user, first_name = data['first_name'], last_name = data['last_name'])
    customerprofile.save()
    return redirect('index:index')

def storeRegister(request):
    if request.user.is_authenticated:
        return redirect('index:index')
    if request.method == 'GET':
        return render(request,'usermanage/register-store.html')
    data = request.POST

     # check user already exits
    if User.objects.filter(username=data['username']).exists():
        return render(request,'usermanage/register-store.html', {
        'user_error' : True,
        })

    user = User.objects.create_user(data['username'], password = data['password'])
    g = Group.objects.get(name='store')
    g.user_set.add(user)
    user.save()
    g.save()
    storeprofile = models.Store(user = user, store_name=data['storename'], profile_image_url=data['profile_image_url'])
    storeprofile.save()
    return redirect_after_login(user)

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

def redirect_after_login(user):
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

@login_required()
@permission_required('usermanage.customer_rights',raise_exception=True)
def customerCoupon(request):
    user = request.user
    coupons = Coupon.objects.filter(user=user)
    context = {
        'coupon':[{
                'name':c.ticket.name,
                'store':c.ticket.store.store.store_name,
                'exp':c.ticket.expire_date.strftime('%Y-%m-%d'),
                'active':c.active,
                'detail':c.ticket.detail,
                'image_url':c.ticket.ticket_image_url
            } for c in coupons]
    }
    return render(request, 'index/coupon.html',context)

@login_required()
@permission_required('usermanage.customer_rights',raise_exception=True)
def customerWallet(request):
    user = request.user
    wallets = [{'name':w.currency.name,'amount':w.amount} for w in Wallet.objects.filter(user=user)]
    print(wallets)
    return render(request, 'index/wallet.html',{'wallets':wallets})
