from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from storemanage.models import Currency, Ticket
from django.utils.dateparse import parse_date
from django.core.validators import URLValidator

import re

def validateTicketForm(data):
    error = {}

    if len(data['name']) > 127:
        error['name_len'] = True
    if int(data['price']) < 0:
        error['price_neg'] = True
    if len(data['detail']) > 1023:
        error['detail_len'] = True
    if data['remaining_day']:
        if int(data['remaining_day']) < 0:
            error['remain_neg'] = True
    # if not URLValidator(data['ticket_image_url']):
    #     error['ticket_url'] = True
    # if not URLValidator(data['content_image_url']):
    #     error['content_url'] = True

    return error

def validateQR(data):
    error = {}
    
    if not re.match(r'\d', data['point']):
        error['digit'] = True

    return error