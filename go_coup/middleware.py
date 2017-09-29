class UserTypeMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print('req:', 'customer' in list(request.user.groups.values_list('name', flat=True)))
        print('req:', 'store' in list(request.user.groups.values_list('name', flat=True)))

        response = self.get_response(request)
        print('res', response)
        # Code to be executed for each request/response after
        # the view is called.

        return response
