from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from storemanage.models import Currency
from django.utils.dateparse import parse_date

@login_required()
@permission_required('usermanage.store_rights',raise_exception=True)
def createQr(request):
    user = request.user
    currency_list = [{'pk':c.pk,'name':c.name} for c in Currency.objects.filter(store=user)]
    if request.method == 'GET':
        return render(request,'store/create-qr.html', {
            'currency_list': currency_list
        })

    data = request.POST
    point = data['point']
    pk_currency = data['currency']
    currency = Currency.objects.get(pk=pk_currency)
    qr = True

    if qr:
        return render(request,'store/create-qr.html', {
            'point': point,
            'currency': currency,
            'currency_list': currency_list,
            'qr': qr
        })