from django.shortcuts import render, get_object_or_404, redirect
from storemanage.models import Currency, Ticket
from usermanage.models import Store
from customermanage.models import Wallet, Coupon
from django.http import HttpResponseBadRequest
# Create your views here.

def purchasable(wallet, ticket):
    if ticket.price > wallet.amount:
        return False
    if ticket.is_limit:
        if ticket.remain <= 0:
            return False
    return True

def purchase(request):
    if request.method == 'GET':
        return HttpResponseBadRequest()
    user = request.user
    ticket_id = request.POST['ticket_id']
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    wallet,create = Wallet.objects.get_or_create(user=user, currency = ticket.currency)
    if purchasable(wallet, ticket):
        wallet.amount -= ticket.price
        wallet.save()
        if ticket.is_limit:
            ticket.remain -= 1
            ticket.save()
        coupon = Coupon(user = user, ticket = ticket)
        coupon.save()
    return redirect('index:detail',ticket_id = ticket_id)
