from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import User, Group

import datetime

from usermanage.models import Customer
from customermanage.models import Coupon
from storemanage.models import Ticket

from social_django.models import UserSocialAuth
from django.db import models

@receiver(post_save, sender = Customer)
def test_handler(sender, **kwargs):
    print(sender)
    print("user created")

@receiver(post_save, sender = Coupon)
def coupon_handler(sender, instance, **kwargs):
    ticket = instance.ticket
    if instance.active:
        if 'purchase_all' not in ticket.stat:
            ticket.stat['purchase_all'] = 0
        ticket.stat['purchase_all'] += 1

        if 'purchase_by_date' not in ticket.stat:
            ticket.stat['purchase_by_date'] = dict()

        today = datetime.date.today().strftime("%Y-%m-%d")

        if today not in ticket.stat['purchase_by_date']:
            ticket.stat['purchase_by_date'][today] = 0

        ticket.stat['purchase_by_date'][today] += 1
    else:
        if 'use_all' not in ticket.stat:
            ticket.stat['use_all'] = 0
        ticket.stat['use_all'] += 1

        if 'use_by_date' not in ticket.stat:
            ticket.stat['use_by_date'] = dict()

        today = datetime.date.today().strftime("%Y-%m-%d")

        if today not in ticket.stat['use_by_date']:
            ticket.stat['use_by_date'][today] = 0

        ticket.stat['use_by_date'][today] += 1

    ticket.save()

@receiver(post_save, sender = UserSocialAuth)
def test_social(sender, instance, **kwargs):
    # print("HELLO")
    # print(instance)
    # print(sender)
    user = instance.user
    # data = {'username':user.username,'email':user.email,'first_name':user.first_name}

    print(user.first_name)
    print(user.last_name)

    groups = list(user.groups.values_list('name', flat=True))
    print('HELLO')
    print(groups)
    check = 'customer' not in groups
    print(check)
    if 'customer' not in groups:
        g = Group.objects.get(name='customer')
        g.user_set.add(user)
        user.save()
        g.save()
        customerprofile = Customer(user = user)
        customerprofile.save()
    # if 'customer' in groups:
    #     g = Group.objects.get(name='customer')
    #     g.user_set.add(user)
    #     user.save()
    #     g.save()
    #     customerprofile = Customer(user = user, )
    #     customerprofile.save()

    # data = {'username':user.username,'email':user.email}
    # if user.groups.filter(name='customer').exists():
    #     customer = models.Customer.objects.get(user=user)
    #     data['first_name']=customer.first_name
    #     data['last_name']=customer.last_name
    # return render(request,'usermanage/profile.html', context={'d':data})


    # user = request.user

    # data = {'username':user.username,'email':user.email}
    # if user.groups.filter(name='store').exists():
    #     store = models.Store.objects.get(user=user)
    #     data['store_name']=store.store_name
    # elif user.groups.filter(name='customer').exists():
    #     customer = models.Customer.objects.get(user=user)
    #     data['first_name']=customer.first_name
    #     data['last_name']=customer.last_name
    # return render(request,'usermanage/profile.html', context={'d':data})

    # customerprofile = models.Customer(user = user, first_name = data['first_name'], last_name = data['last_name'])
    # customerprofile.save()
    # return redirect('index:index')



