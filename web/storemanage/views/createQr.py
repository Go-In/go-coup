from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from storemanage.models import Currency
from django.utils.dateparse import parse_date

from .validateForm import validateQR

import requests

@login_required()
@permission_required('usermanage.store_rights',raise_exception=True)
def createQr(request):
    user = request.user
    currency_list = [{'pk':c.pk,'name':c.name} for c in Currency.objects.filter(store=user)]
    qr = False
    if request.method == 'GET':
        return render(request,'store/create-qr.html', {
            'currency_list': currency_list,
            'qr': qr
        })

    #get data from input
    data = request.POST

    #validate point
    error = validateQR(data)

    if not currency_list:
        error['currency'] = True

    if error:
        return render(request, 'store/create-qr.html', {
        'error': error,
        'currency_list': currency_list
    })


    point = data['point']
    pk_currency = data['currency']
    currency = Currency.objects.get(pk=pk_currency)
    payload = {'price':point, 'currency':pk_currency, 'reuse':'true'}

    #generate redeem code url
    url_gencode = 'http://codegen:8081/save'
    req = requests.post(url_gencode, data=payload)
    key = req.json()['Key']
    url_redeem = "http://localhost:8000/get-point/" + str(user) + "/" + key + "/"

    # show qr code alert
    qr = True

    if qr:
        return render(request,'store/create-qr.html', {
            'point': point,
            'currency': currency,
            'currency_list': currency_list,
            'pk_currency': pk_currency,
            'qr': qr,
            'url_redeem': url_redeem,
        })