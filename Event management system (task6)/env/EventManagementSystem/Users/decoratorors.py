from django.http import HttpResponseForbidden

def permissions_needed(permissions=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            for permission in permissions:
                if permission not in request.user.permissions:
                    return HttpResponseForbidden("You don't have permission to access this page")
            return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator


