from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from usermanage.models import Customer, Store
from django.utils.dateparse import parse_date
from django.core.validators import URLValidator
from usermanage import models
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

def validateStoreForm(data):
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

def validateCustomerForm(data):
    error = {}
    if User.objects.filter(username = data['username']).exists():
        error['user_exist'] = True
    if len(data['username']) > 30:
        error['user_len'] = True
    # if not URLValidator(data['profile_image_url']):
    #     error['url'] = True
    if len(data['first_name']) > 30:
        error['firstname_len'] = True
    if len(data['last_name']) > 30:
        error['lastname_len'] = True
    if len(data['tel']) > 12:
        error['tel_len'] = True
    try:
        validate_email(data['email'])
    except ValidationError as e:
        error['email'] = True

    return error