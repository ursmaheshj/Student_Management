from django.contrib.auth import authenticate,login,logout
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.contrib import messages
from Main_App.EmailAuthentication import EmailAuth

# Create your views here.

def index(request):
    return render(request, 'index.html')

def loginpage(request):
    return render(request,'loginpage.html')

def loginuser(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not allowed</h2>")
    else : 
        user = EmailAuth.authenticate(request,username=request.POST.get('email'),password=request.POST.get('password'))
        if user!=None:
            login(request,user)
            if user.user_type=='1':
                return HttpResponseRedirect('/adminhome')
            elif user.user_type=='2':
                return HttpResponseRedirect('/teacherhome')
            elif user.user_type=='3' :
                return HttpResponseRedirect('/studenthome')
            else :
                return HttpResponse("Invalid user type")
        else :
            messages.error(request,"Invalid login details..!")
            return HttpResponseRedirect("/loginpage")

def logoutuser(request):
    logout(request)
    return HttpResponseRedirect('/')