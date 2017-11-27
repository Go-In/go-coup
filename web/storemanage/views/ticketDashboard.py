from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from storemanage.models import Currency, Ticket
from django.utils.dateparse import parse_date

@login_required()
@permission_required('usermanage.store_rights',raise_exception=True)
def ticketDashboard(request, ticket_id):
    return render(request, 'store/dashboard.html', {})
