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
def customerCoupon(request):
    user = request.user
    coupons = Coupon.objects.filter(user=user)
    context = {
        'coupon':[{
                'name':c.ticket.name,
                'store':c.ticket.store.store.store_name,
                'exp':c.ticket.expire_date.strftime('%Y-%m-%d'),
                'active':c.active,
                'detail':c.ticket.detail,
                'image_url':c.ticket.ticket_image_url
            } for c in coupons]
    }
    return render(request, 'index/coupon.html',context)
