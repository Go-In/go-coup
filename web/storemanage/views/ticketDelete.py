from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from storemanage.models import Currency, Ticket
from django.utils.dateparse import parse_date

@login_required()
@permission_required('usermanage.store_rights',raise_exception=True)
def ticketDelete(request, ticket_id):
    user = request.user
    ticket = Ticket.objects.get(pk=ticket_id)
    if ticket.store != user:
        return index(request, 'ไม่มีสิทธิในการเข้าถึง ticket นี้')
    setattr(ticket, 'available', False)
    ticket.save()
    return redirect('store:index')
