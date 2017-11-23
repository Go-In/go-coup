from django.shortcuts import render, redirect
from django.contrib.staticfiles.views import serve
from storemanage.models import Ticket, Currency
from customermanage.models import Wallet, Qrcode

from django.http import JsonResponse

import requests

def getCoupon(request):
    return render(request, 'store/get-coupon.html', {
            
        })