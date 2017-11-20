from django.shortcuts import render, redirect
from storemanage.models import Ticket
from usermanage.models import Store

from django.http import JsonResponse

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
    print('store: ', ticket.store.id)
    return render(request, 'index/detail.html', {
        'ticket': ticket,
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

def store(request, store_id):
    user = request.user
    print('store id:', store_id)
    store = Store.objects.get(pk=store_id)
    tickets = Ticket.objects.filter(store=user)
    return render(request, 'index/store.html', {
        'tickets': tickets,
        'store': store,
    })

def brand_list(request):
    user = request.user
    stores = Store.objects.filter(available=True)
    return render(request, 'index/brand-list.html', {
        'stores' : stores,
    })