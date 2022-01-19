from django.http import HttpResponse
from django.shortcuts import redirect

from Main_App.models import MyUser

def is_authenticated(func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return func(request,*args,**kwargs)
        else:
            return redirect('/loginpage')
    return wrapper

def is_admin(func):
    def wrapper(request,*args,**kwargs):
        try:
            user = MyUser.objects.get(id=request.user.id)
            if user.user_type == '1':
                return func(request,*args,**kwargs)
            else:
                return HttpResponse("<h3>You are not authorised to view this page</h3>")
        except:
            return HttpResponse("<h3>You are not authorised to view this page.</h3>")
    return wrapper

def is_teacher(func):
    def wrapper(request,*args,**kwargs):
        try:
            user = MyUser.objects.get(id=request.user.id)
            if user.is_teacher == True:
                return func(request,*args,**kwargs)
            else:
                return HttpResponse("<h3>You are not authorised to view this page</h3>")
        except:
            return HttpResponse("<h3>You are not authorised to view this page.</h3>")
    return wrapper

def is_student(func):
    def wrapper(request,*args,**kwargs):
        try:
            user = MyUser.objects.get(id=request.user.id)
            if user.is_student == True:
                return func(request,*args,**kwargs)
            else:
                return HttpResponse("<h3>Log in as student to view this page</h3>")
        except:
            return HttpResponse("<h3>Log in as student to view this page.</h3>")
    return wrapper