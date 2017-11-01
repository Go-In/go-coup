from django.shortcuts import render, redirect
from storemanage.models import Currency
from customermanage.models import Wallet
# Create your views here.
def motherload(request):
    if request.method == 'GET':
        currency_list = [{'pk':c.pk,'name':c.name} for c in Currency.objects.all()]
        context = {
            'currency_list': currency_list
        }
        return render(request,'customermanage/motherload.html',context)
    user = request.user
    data = request.POST
    currency = Currency.objects.get(pk=data['currency'])
    wallet,create = Wallet.objects.get_or_create(user=user, currency = currency)
    wallet.amount = (wallet.amount if not create else 0) + int(data['amount'])
    wallet.save()
    return redirect('index:index')
