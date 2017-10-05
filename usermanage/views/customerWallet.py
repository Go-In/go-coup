from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.forms import UserCreationForm
from customermanage.models import Coupon, Wallet
from storemanage.models import Ticket
# Create your views here.
from usermanage import models

@login_required()
@permission_required('usermanage.customer_rights',raise_exception=True)
def customerWallet(request):
    user = request.user
    wallets = [{'name':w.currency.name,'amount':w.amount} for w in Wallet.objects.filter(user=user)]
    print(wallets)
    return render(request, 'index/wallet.html',{'wallets':wallets})
