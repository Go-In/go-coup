from django.shortcuts import render, get_object_or_404
from storemanage.models import Currency, Ticket
from usermanage.models import Store
from customermanage.models import Wallet
from django.http import HttpResponseBadRequest
# Create your views here.

def purchase(request):
    if request.method == 'GET':
        return HttpResponseBadRequest()
    user = request.user
    ticket_id = request.POST['ticket_id']
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    return render('index:index')
