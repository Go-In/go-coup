from django.shortcuts import render
from storemanage.models import Ticket

# Create your views here.
def index(request):
    tickets = Ticket.objects.all()
    a = [];
    for i in range(10):
        a.append(tickets[0])
    print(a)
    return render(request, 'index/index.html', {
        'tickets': a
    })

def detail(request, coupon_id):
    return render(request, 'index/detail.html', {})

def profile(request):
    return render(request, 'index/profile.html', {})

def cart(request):
    return render(request, 'index/cart.html', {})

def coupon(request):
    return render(request, 'index/coupon.html', {})

def setting(request):
    return render(request, 'index/setting.html', {})

def wallet(request):
    return render(request, 'index/wallet.html', {})

def login(request):
    return render(request, 'index/login.html', {})
