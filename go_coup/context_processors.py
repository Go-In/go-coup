def groups(request):
    groups = list(request.user.groups.values_list('name', flat=True)
    return {'isCustomer':'customer' in groups, 'isStore':'store' in groups}
