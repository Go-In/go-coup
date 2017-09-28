from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Currency, Ticket
from django.utils.dateparse import parse_date

# Create your views here.
def currencyRegister(request):
    user = request.user
    if request.method == 'GET':
        return render(request,'storemanage/currency-form.html')
    data = request.POST
    currency = Currency(store=user,name=data['name'])
    currency.save()
    return redirect('index:index')

def ticketRegister(request):
    user = request.user
    if request.method == 'GET':
        print('GET')
        currency_list = [{'pk':c.pk,'name':c.name} for c in Currency.objects.filter(store=user)]
        context = {
            'currency_list':currency_list
            }
        return render(request,'storemanage/ticket-form.html',context)
    data = request.POST
    ticket_attrib = {k:v for k,v in data.items() if v != ''}
    ticket_attrib.pop('csrfmiddlewaretoken')
    ticket_attrib['is_period'] = True if 'is_period' in ticket_attrib else False
    ticket_attrib['is_limit'] = True if 'is_limit' in ticket_attrib else False
    ticket_attrib['currency'] = Currency.objects.get(pk=ticket_attrib['currency'])
    ticket_attrib['store'] = user
    ticket = Ticket(**ticket_attrib)
    ticket.save()
    return redirect('index:index')
