from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.forms import UserCreationForm
from customermanage.models import Coupon, Wallet
from storemanage.models import Ticket
from django.core.urlresolvers import reverse
# Create your views here.
from usermanage import models
from go_coup.host import host_url

import requests

@login_required()
@permission_required('usermanage.customer_rights',raise_exception=True)
def customerCoupon(request):
    user = request.user
    coupons = Coupon.objects.filter(user=user, active=True)
    coupon_url = []
    for c in coupons:
        #generate redeem code url
        url_gencode = 'http://coupon-qr-gen:8082/save'
        payload = {'pk': c.id}
        req = requests.post(url_gencode, data=payload)
        key = req.json()['Key']

        path_coupon = str(reverse('store:get-coupon', args=(user, key)))
        url_use_coupon = host_url + path_coupon
        coupon_url.append(url_use_coupon)
    print(coupon_url)

    context = {
        'coupon':[{
                'name':c.ticket.name,
                'store':c.ticket.store.store.store_name,
                'exp':c.ticket.expire_date.strftime('%Y-%m-%d'),
                'active':c.active,
                'detail':c.ticket.detail,
                'image_url':c.ticket.ticket_image_url
            } for c in coupons],
        'coupon_url':coupon_url
    }
    return render(request, 'index/coupon.html', context)
