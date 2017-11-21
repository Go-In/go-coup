from django.shortcuts import render, redirect
from django.contrib.staticfiles.views import serve
from storemanage.models import Ticket, Currency
from customermanage.models import Wallet

from django.http import JsonResponse

import requests

# Create your views here.
def index(request):
    success = request.session.get('success')
    fail = request.session.get('fail')
    if success:
        request.session['success'] = False
    if fail:
        request.session['fail'] = False
    tickets = Ticket.objects.filter(available=True)
    return render(request, 'index/index.html', {
        'tickets': tickets,
        'success': success,
        'fail': fail
    })
def sw(request):
    return serve(request, '../static/sw.js')

def detail(request, ticket_id):
    success = request.session.get('success')
    fail = request.session.get('fail')
    if success:
        request.session['success'] = False
    if fail:
        request.session['fail'] = False
    ticket = Ticket.objects.get(pk=ticket_id)
    if ticket.available == False:
        return redirect('index:index')
    return render(request, 'index/detail.html', {
        'ticket' : ticket,
        'success': success,
        'fail': fail
    })

def cart(request):
    data = request.GET
    if 'cart' not in data:
        return redirect('index:index')
    items = data['cart'].split(',') if data['cart'] else []
    tickets = Ticket.objects.filter(pk__in=items)
    return render(request, 'index/cart.html', {
        'tickets': tickets
    })

def catalog(request):
    tickets = Ticket.objects.filter(available=True)
    return render(request, 'index/catalog.html', {
        'tickets': tickets
    })

# def search(request):
#     return render(request, 'index/search.html')

def searchDemo(request):
    data = request.POST
    if not 'search_name' in data:
        return redirect('index:index')
    name = data['search_name']
    tickets = Ticket.objects.filter(name__search=name)
    for i in tickets:
        print(i.detail)
    return render(request, 'index/search-demo.html', {
        'tickets' : tickets
    })

def getPoint(request, store, key):
    user = request.user
    print(user)

    url_redeem = 'http://codegen:8081/load'
    payload = {'key': key}
    req = requests.post(url_redeem, data=payload)
    print(req.json())
    can_redeem = False

    if req.json()['Status'] != 'NOT_FOUND':
        price = req.json()['Value']['Price']
        pk_currency = req.json()['Value']['Currency']
        reuse = req.json()['Value']['Reuse']
        currency = Currency.objects.get(pk=pk_currency)

        wallet,create = Wallet.objects.get_or_create(user=user, currency=currency)
        wallet.amount = (wallet.amount if not create else 0) + int(price)
        wallet.save()

        can_redeem = True

        return render(request, 'index/get-point.html', {
            'price': price,
            'currency': currency,
            'reuse': reuse,
            'can_redeem': can_redeem
        })
    else:
        return render(request, 'index/get-point.html', {
            'can_redeem': can_redeem
        })