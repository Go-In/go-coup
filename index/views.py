from django.shortcuts import render
from storemanage.models import Ticket
from django import forms
from django.http import JsonResponse

from .forms import NameForm
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

def cart(request):
    data = request.GET
    items = data['cart'].split(',') if data['cart'] else []
    tickets = Ticket.objects.filter(pk__in=items)
    return render(request, 'index/cart.html', {
        'tickets': tickets
    })

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