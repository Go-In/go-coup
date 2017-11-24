from django.shortcuts import render, redirect
from django.contrib.staticfiles.views import serve
from storemanage.models import Ticket, Currency
from customermanage.models import Coupon

from django.http import JsonResponse

import requests

def getCoupon(request, key):
    url_get_pk = 'http://coupon-qr-gen:8082/load'
    payload = {'key':  key}
    req = requests.post(url_get_pk, data=payload)
    pk = req.json()['Pk']

    coupon = Coupon.objects.get(id=pk)
    coupon.active = False
    coupon.save()

    return render(request, 'store/get-coupon.html', {
            'coupon': coupon
        })