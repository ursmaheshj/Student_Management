#from django.contrib.auth import authenticate,login,logout
from django.contrib import admin, messages
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from Main_App.models import MyUser, Notification,Teacher, Student

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


def editteacher(request,teacher_id):
    teacher = Teacher.objects.get(admin=teacher_id)
    return render(request,'admin/a_editteacher.html',{'teacher':teacher})


def saveeditteacher(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed..!")
    else :
        teacher_id = request.POST.get('teacher_id')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        try :
            user = MyUser.objects.get(id=teacher_id)
            #create_user(username=username,email=email,first_name=firstname,last_name=lastname,user_type=2)
            user.first_name=firstname
            user.last_name=lastname
            user.email=email      
            user.save()

            teacher = Teacher.objects.get(admin=teacher_id)
            teacher.address=address
            teacher.gender=gender  
            teacher.save()
            messages.success(request,"Teacher Updated successfully")
            return HttpResponseRedirect("/editteacher/"+teacher_id)
        except :
            messages.error(request,"Failed to Update teacher")
            return HttpResponseRedirect("/editteacher"+teacher_id)



def editstudent(request,student_id):
    student = Student.objects.get(admin=student_id)
    return render(request,'admin/a_editstudent.html',{'student':student})


def saveeditstudent(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed..!")
    else :
        student_id = request.POST.get('student_id')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        medium = request.POST.get('medium')
        std = request.POST.get('std')
        try :
            user = MyUser.objects.get(id=student_id)
            user.email=email
            user.first_name=firstname
            user.last_name=lastname
            user.save()

            student = Student.objects.get(admin=student_id)
            student.address=address
            student.gender=gender   
            student.medium=medium 
            student.std=std      
            student.save()
            
            messages.success(request,"Student upadated successfully")
            return HttpResponseRedirect("/editstudent/"+student_id)
        except :
            messages.error(request,"Failed to update student")
            return HttpResponseRedirect("/editstudent/"+student_id)

def a_addnotification(request):
    return render(request,'admin/a_addnotification.html')


def savenotification(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed..!")
    else :
        heading = request.POST.get('heading')
        message = request.POST.get('message')
        created_by = request.user.first_name
        try :
            
            notification = Notification.objects.create(heading=heading,message=message,created_by=created_by)
            notification.save()
            
            messages.success(request,"Notification added successfully")
            return HttpResponseRedirect("/a_addnotification")
        except :
            messages.error(request,"Failed to add Notification")
            return HttpResponseRedirect("/a_addnotification")

def managenotification(request):
    notifications = Notification.objects.all()
    return render(request,'admin/a_managenotification.html',{'notifications':notifications})
