from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from storemanage.models import Currency, Ticket
from django.utils.dateparse import parse_date

def validateForm(data):
    error = {}
    if not data['name']:
        error['name'] = True
    if not data['detail']:
        error['price'] = True
    if not data['expire_date']:
        error['expire_date'] = True
    if not data['currency']:
        error['currency'] = True
    if not data['ticket_image_url']:
        error['ticket_image_url'] = True
    if not data['content_image_url']:
        error['content_image_url'] = True
    return error
