from django.shortcuts import redirect
from django.http import HttpResponse

def allowed_user_types(allowed_user_types=[]):
    def wrapper1(view_func):
        def wrapper2(request, *args, **kwargs):
            groups = []

            if request.user.groups.exists():
                for group in request.user.groups.all():
                    groups.append(group.name)


            for group in groups:
                if group in allowed_user_types:
                    return view_func(request, *args, **kwargs)
            
            return HttpResponse("Unauthorized.")

        return wrapper2
    return wrapper1
