from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from storemanage.models import Currency, Ticket
from django.utils.dateparse import parse_date

from .validateForm import validateTicketForm

@login_required()
@permission_required('usermanage.store_rights',raise_exception=True)
def ticketRegister(request):
    user = request.user
    currency_list = [{'pk':c.pk,'name':c.name} for c in Currency.objects.filter(store=user)]
    if request.method == 'GET':
        return render(request,'store/add.html', {
            'currency_list': currency_list
        })
    data = request.POST

    error = validateTicketForm(data)

    if not currency_list:
        error['currency'] = True

    if error:
        return render(request,'store/add.html', {
            'error': error,
            'currency_list':currency_list
        })  
    # print(data.items())
    ticket_attrib = {k:v for k,v in data.items() if v != ''}
    ticket_attrib.pop('csrfmiddlewaretoken')
    ticket_attrib['is_period'] = True if 'is_period' in ticket_attrib else False
    ticket_attrib['is_limit'] = True if 'is_limit' in ticket_attrib else False
    ticket_attrib['currency'] = Currency.objects.get(pk=ticket_attrib['currency'])
    ticket_attrib['store'] = user
    ticket = Ticket(**ticket_attrib)
    ticket.save()
    return redirect('store:index')
