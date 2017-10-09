from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from storemanage.models import Currency, Ticket
from django.utils.dateparse import parse_date

from .validateForm import validateTicketForm

@login_required()
@permission_required('usermanage.store_rights',raise_exception=True)
def ticketEdit(request, ticket_id):
    user = request.user
    currency_list = [{'pk':c.pk,'name':c.name} for c in Currency.objects.filter(store=user)]
    ticket = Ticket.objects.get(pk=ticket_id)

    if ticket.store != user:
        return index(request, 'ไม่มีสิทธิในการเข้าถึง ticket นี้')

    if request.method == 'GET':
        return render(request, 'store/edit.html', {
            'ticket': ticket,
            'currency_list':currency_list
        })
    data = request.POST
    error = validateTicketForm(data)
    if error:
        return render(request,'store/edit.html', {
            'error': error,
            'currency_list':currency_list
        })
    for k, v in data.items():
        if v != '' and k != 'csrfmiddlewaretoken':
            if k == 'currency':
                setattr(ticket,k, Currency.objects.get(pk=v))
            else:
                setattr(ticket,k, v)

    if 'is_period' in data.keys():
        setattr(ticket, 'is_period', True)
    else:
        setattr(ticket, 'is_period', False)

    if 'is_limit' in data.keys():
        setattr(ticket, 'is_limit', True)
    else:
        setattr(ticket, 'is_limit', False)
    ticket.save()
    return redirect('store:index')
