from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from usermanage.models import Customer, Store
from django.utils.dateparse import parse_date
from django.core.validators import URLValidator
from usermanage import models

def validateForm(data):
    error = {}
    if User.objects.filter(username = data['username']).exists():
        error['user_exist'] = True
    if models.Store.objects.filter(store_name = data['storename']).exists():
        error['store_exist'] = True
    if len(data['username']) > 30:
        error['user_len'] = True
    if len(data['storename']) > 30:
        error['store_len'] = True
    # if not URLValidator(data['profile_image_url']):
    #     error['url'] = True
    return error