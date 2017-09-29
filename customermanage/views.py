from django.shortcuts import render
from storemanage.models import Currency
# Create your views here.
def motherload(request):
    currency_list = [{'pk':c.pk,'name':c.name} for c in Currency.objects.all()]
    context = {
        'currency_list': currency_list
    }
    return render(request,'customermanage/motherload.html',context)
