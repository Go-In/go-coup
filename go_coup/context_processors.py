def groups(request):
    groups = list(request.user.groups.values_list('name', flat=True))
    return {'is_customer':'customer' in groups, 'is_store':'store' in groups}
