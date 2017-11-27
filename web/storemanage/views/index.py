import requests
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from storemanage.models import Currency, Ticket
from django.utils.dateparse import parse_date

@login_required()
@permission_required('usermanage.store_rights',raise_exception=True)
def index(request, error=''):
    user = request.user
    tickets = Ticket.objects.filter(store=user, available=True)
    r = requests.get('http://notification:8080/subscribe/list/' + str(user.id))
    return render(request,'store/index.html', {
        'user': user,
        'tickets': tickets,
        'error': error,
        'subscribes_len': len(r.json())
    })
