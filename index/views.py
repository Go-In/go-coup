from django.shortcuts import render
from storemanage.models import Ticket
from django.http import JsonResponse

# Create your views here.
def index(request):
    tickets = Ticket.objects.all()
    return render(request, 'index/index.html', {
        'tickets': tickets
    })

def detail(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    return render(request, 'index/detail.html', {
        'ticket' : ticket
    })

def profile(request):
    return render(request, 'index/profile.html', {})

def cart(request):
    data = request.GET
    items = data['cart'].split(',')
    tickets = Ticket.objects.filter(pk__in=items)
    return render(request, 'index/cart.html', {
        'tickets': tickets
    })

def coupon(request):
    return render(request, 'index/coupon.html', {})

def setting(request):
    return render(request, 'index/setting.html', {})

def wallet(request):
    return render(request, 'index/wallet.html', {})

def login(request):
    return render(request, 'index/login.html', {})
