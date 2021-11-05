#from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from Main_App.models import MyUser, Teacher, Student


# Create your views here.

def a_home(request):
    return render(request,'admin/a_home.html')

def addteacher(request):
    genders = Teacher.gender_choices
    return render(request,'admin/a_addteacher.html',{'genders':genders})

def saveteacher(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed..!")
    else :
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
    try :
        user = MyUser.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname,user_type=2)
        user.teacher.address=address
        user.teacher.gender=gender        
        user.save()
        
        messages.success(request,"Teacher added successfully")
        return HttpResponseRedirect("/addteacher")
    except :
        messages.error(request,"Failed to add teacher")
        return HttpResponseRedirect("/addteacher")

def addstudent(request):
    genders = Student.gender_choices
    stds = Student.std_choices
    mediums = Student.medium_choices
    return render(request,'admin/a_addstudent.html',{'genders':genders,'stds':stds,'mediums':mediums})

def savestudent(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed..!")
    else :
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        medium = request.POST.get('medium')
        std = request.POST.get('std')
    try :
        user = MyUser.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname,user_type=3)
        user.student.address=address
        user.student.gender=gender   
        user.student.medium=medium 
        user.student.std=std      
        user.save()
        
        messages.success(request,"Student added successfully")
        return HttpResponseRedirect("/addstudent")
    except :
        messages.error(request,"Failed to add student")
        return HttpResponseRedirect("/addstudent")

def manageteacher(request):
    teachers = Teacher.objects.all()
    return render(request,'admin/a_manageteacher.html',{'teachers':teachers})

def managestudent(request):
    students = Student.objects.all()
    return render(request,'admin/a_managestudent.html',{'students':students})
