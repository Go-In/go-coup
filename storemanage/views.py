from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from .models import Currency, Ticket
from django.utils.dateparse import parse_date

@login_required()
@permission_required('usermanage.store_rights',raise_exception=True)
def index(request, error=''):
    user = request.user
    tickets = Ticket.objects.filter(store=user)
    return render(request,'store/index.html', {
        'user': user,
        'tickets': tickets,
        'error': error
    })

@login_required()
@permission_required('usermanage.store_rights',raise_exception=True)
def currencyRegister(request):
    user = request.user
    if request.method == 'GET':
        return render(request,'storemanage/currency-form.html')
    data = request.POST
    currency = Currency(store=user,name=data['name'])
    currency.save()
    return redirect('index:index')

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

@login_required()
@permission_required('usermanage.store_rights',raise_exception=True)
def ticketRegister(request):
    user = request.user
    currency_list = [{'pk':c.pk,'name':c.name} for c in Currency.objects.filter(store=user)]
    if request.method == 'GET':
        return render(request,'store/add.html', {
            'currency_list': currency_list
        })
    data = request.POST
    error = validateForm(data)
    if error:
        return render(request,'store/add.html', {
            'error': error,
            'currency_list':currency_list
        })
    print(data.items())
    ticket_attrib = {k:v for k,v in data.items() if v != ''}
    ticket_attrib.pop('csrfmiddlewaretoken')
    ticket_attrib['is_period'] = True if 'is_period' in ticket_attrib else False
    ticket_attrib['is_limit'] = True if 'is_limit' in ticket_attrib else False
    ticket_attrib['currency'] = Currency.objects.get(pk=ticket_attrib['currency'])
    ticket_attrib['store'] = user
    ticket = Ticket(**ticket_attrib)
    ticket.save()
    return redirect('store:index')

@login_required()
@permission_required('usermanage.store_rights',raise_exception=True)
def ticketEdit(request, ticket_id):
    user = request.user
    currency_list = [{'pk':c.pk,'name':c.name} for c in Currency.objects.filter(store=user)]
    ticket = Ticket.objects.get(pk=ticket_id)
    if ticket.store != user:
        return index(request, 'ไม่มีสิทธิในการเข้าถึง ticket นี้')
    if request.method == 'GET':
        return render(request, 'store/edit.html', {
            'ticket': ticket,
            'currency_list':currency_list
        })
    data = request.POST
    error = validateForm(data)
    if error:
        return render(request,'store/edit.html', {
            'error': error,
            'currency_list':currency_list
        })
    for k, v in data.items():
        if v != '' and k != 'csrfmiddlewaretoken':
            if k == 'currency':
                setattr(ticket,k, Currency.objects.get(pk=v))
            else:
                setattr(ticket,k, v)
    
    if 'is_period' in data.keys():
        setattr(ticket, 'is_period', True)
    else:
        setattr(ticket, 'is_period', False)
    
    if 'is_limit' in data.keys():
        setattr(ticket, 'is_limit', True)
    else:
        setattr(ticket, 'is_limit', False)    

    ticket.save()
    return redirect('store:index')

@login_required()
@permission_required('usermanage.store_rights',raise_exception=True)
def ticketDelete(request, ticket_id):
    user = request.user
    ticket = Ticket.objects.get(pk=ticket_id)
    if ticket.store != user:
        return index(request, 'ไม่มีสิทธิในการเข้าถึง ticket นี้')
    # ticket.delete()
    return redirect('store:index')
