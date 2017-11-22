from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from django.conf import settings

import datetime

from usermanage.models import Customer
from customermanage.models import Coupon
from storemanage.models import Ticket

@receiver(post_save, sender = Customer)
def test_handler(sender, **kwargs):
    print(sender)
    print("user created")

@receiver(post_save, sender = Coupon)
def coupon_handler(sender, instance, **kwargs):
    ticket = instance.ticket
    if 'purchase_all' not in ticket.stat:
        ticket.stat['purchase_all'] = 0
    ticket.stat['purchase_all'] += 1

    if 'purchase_by_date' not in ticket.stat:
        ticket.stat['purchase_by_date'] = dict()

    today = datetime.date.today().strftime("%Y-%m-%d")

    if today not in ticket.stat['purchase_by_date']:
        ticket.stat['purchase_by_date'][today] = 0

    ticket.stat['purchase_by_date'][today] += 1

    ticket.save()
    print(ticket)
