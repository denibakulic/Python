from.models import MyUser
from django.shortcuts import redirect

def mentor_required(function):
    def wrap (request, *args, **kwargs):
        if request.user.role == "MENTOR":
            return function(request, *args, **kwargs)
        else:
            return redirect('login')
    return wrap

def student_required(function):
    def wrap (request, *args, **kwargs):
        if request.user.role == "STUDENT":
            return function(request, *args, **kwargs)
        else:
            return redirect('login')
    return wrap