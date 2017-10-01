from django.shortcuts import render, redirect
from storemanage.models import Ticket

from django.http import JsonResponse

# Create your views here.
def index(request):
    tickets = Ticket.objects.all()
    return render(request, 'index/index.html', {
        'tickets': tickets
    })

def detail(request, ticket_id):
    success = request.session.get('success')
    if success:
        request.session['success'] = False
    ticket = Ticket.objects.get(pk=ticket_id)
    return render(request, 'index/detail.html', {
        'ticket' : ticket,
        'success': success
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
    tickets = Ticket.objects.all()
    return render(request, 'index/catalog.html', {
        'tickets': tickets

      def search(request):
    return render(request, 'index/search.html', {})

def searchDemo(request):
    data = request.POST
    name = data['search_name']

    tickets = Ticket.objects.filter(name__search=name)

    for i in tickets:
        print(i.detail)

    return render(request, 'index/search-demo.html', {
        'tickets' : tickets
    })