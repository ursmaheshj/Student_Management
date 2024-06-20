from datetime import date
from random import randint
from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.conf import settings
from django.core.mail.message import EmailMessage
from django.template.loader import render_to_string

from Main_App.models import MyUser, Notes, Notification, Student ,Result, Teacher
from Main_App.restrictions import is_authenticated, is_teacher

@is_authenticated
@is_teacher
def t_home(request):
    marathi_count = Student.objects.filter(medium='Marathi').count()
    semi_count = Student.objects.filter(medium='SemiEng').count()
    cbse_count = Student.objects.filter(medium='CBSE').count()
    foundation_count = Student.objects.filter(medium='Foundation').count()

    male_count = Student.objects.filter(gender="Male").count()
    female_count = Student.objects.filter(gender="Female").count()
    other_count = Student.objects.filter(gender="Other").count()

    count_1 = Student.objects.filter(std=1).count()
    count_2 = Student.objects.filter(std=2).count()
    count_3 = Student.objects.filter(std=3).count()
    count_4 = Student.objects.filter(std=4).count()
    count_5 = Student.objects.filter(std=5).count()
    count_6 = Student.objects.filter(std=6).count()
    count_7 = Student.objects.filter(std=7).count()
    count_8 = Student.objects.filter(std=8).count()
    count_9 = Student.objects.filter(std=9).count()
    count_10 = Student.objects.filter(std=10).count()

    context = {
        "marathi_count":marathi_count,
        "semi_count":semi_count,
        "cbse_count":cbse_count,
        "foundation_count":foundation_count,

        "male_count":male_count,
        "female_count":female_count,
        "other_count":other_count, 

        "count_1":count_1,
        "count_2":count_2,
        "count_3":count_3,
        "count_4":count_4,
        "count_5":count_5,
        "count_6":count_6,
        "count_7":count_7,
        "count_8":count_8,
        "count_9":count_9,
        "count_10":count_10,
    }
    return render(request,'teacher/t_home.html',context)

@is_authenticated
@is_teacher
def t_profile(request):
    return render(request,'teacher/t_profile.html')

@is_authenticated
@is_teacher
def t_saveprofile(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed..!")
    else :
        teacher_id = request.POST.get('teacher_id')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        try :
            user = MyUser.objects.get(id=teacher_id)
            user.first_name=firstname
            user.last_name=lastname
            user.email=email  
            if password != None and password != "":
                user.set_password(password)
            user.save()

            teacher = Teacher.objects.get(admin=teacher_id)
            teacher.address=address
            teacher.gender=gender  
            teacher.save()
            messages.success(request,"Profile Updated successfully")
            return HttpResponseRedirect('/teacherprofile')
        except :
            messages.error(request,"Failed to Update Profile")
            return HttpResponseRedirect('/teacherprofile')

@is_authenticated
@is_teacher
def t_addstudent(request):
    genders = Student.gender_choices
    stds = Student.std_choices
    mediums = Student.medium_choices
    return render(request,'teacher/t_addstudent.html',{'genders':genders,'stds':stds,'mediums':mediums})

@is_authenticated
@is_teacher
def t_savestudent(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed..!")
    else :
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        medium = request.POST.get('medium')
        std = request.POST.get('std')
        password = "Student@100"
        def random_username():
            r=randint(1000,9999)
            username = "SC"+str(date.today().year)+str(r)
            try:
                if MyUser.objects.filter(username=username).exists():
                    return random_username()
                else :
                    return username
            except :
                messages.error(request,"Student code failure")
                return HttpResponseRedirect("/addstudent")
        try :
            username = random_username()
            user = MyUser.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname,user_type=3)
            user.student.address=address
            user.student.gender=gender   
            user.student.medium=medium 
            user.student.std=std      
            user.save()

            # template = render_to_string('base/email_template.html',{'name':firstname,'username':username,'password':password})
            # email = EmailMessage(
            #     'Your account created successfully!',
            #     template,
            #     settings.EMAIL_HOST_USER,
            #     [email]
            # )
            # email.fail_silently = False
            # email.send()

            messages.success(request,"Student added successfully")
            return HttpResponseRedirect("/t_addstudent")
        except :
            messages.error(request,"Failed to add student")
            return HttpResponseRedirect("/t_addstudent")

@is_authenticated
@is_teacher
def t_viewstudent(request):
    students = Student.objects.all()
    return render(request,'teacher/t_viewstudent.html',{'students':students})

@is_authenticated
@is_teacher
def t_resetspass(request,student_id):
    try:
        user = MyUser.objects.get(id=student_id)
        user.set_password("Student@100")
        messages.success(request,"Password reset successfully to Student@100")
        return HttpResponseRedirect("/t_viewstudent")
    except :
        messages.error(request,"Failed to reset password")
        return HttpResponseRedirect("/t_viewstudent")

@is_authenticated
@is_teacher
def t_addnotification(request):
    return render(request,'teacher/t_addnotification.html')

@is_authenticated
@is_teacher
def t_savenotification(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed..!")
    else :
        
        try :
            heading = request.POST.get('heading')
            message = request.POST.get('message')
            created_by = request.user.username

            notification = Notification.objects.create(heading=heading,message=message,created_by=created_by)
            notification.save()
            
            messages.success(request,"Notification added successfully")
            return HttpResponseRedirect("/t_addnotification")
        except :
            messages.error(request,"Failed to add Notification")
            return HttpResponseRedirect("/t_addnotification")

@is_authenticated
@is_teacher
def t_deletenotification(request):
    try: 
        notifications = Notification.objects.filter(created_by=request.user.username)
        return render(request,'teacher/t_deletenotification.html',{'notifications':notifications})
    except:
        return render(request,'teacher/t_deletenotification.html')

@is_authenticated
@is_teacher
def t_removenotification(request,notification_id):
    notification = Notification.objects.get(id=notification_id)
    try:
        notification.delete()
        messages.success(request,"Notification deleted successfully")
        return HttpResponseRedirect("/t_deletenotification")
    except :
        messages.error(request,"Failed to delete Notification")
        return HttpResponseRedirect("/t_deletenotification")

@is_authenticated
@is_teacher
def t_viewnotification(request):
    try: 
        notifications = Notification.objects.all()
        return render(request,'teacher/t_viewnotification.html',{'notifications':notifications})
    except:
        return render(request,'teacher/t_viewnotification.html')

@is_authenticated
@is_teacher
def t_addresult(request):
    stds = Result.std_choices
    mediums = Result.medium_choices
    return render(request,'teacher/t_addresult.html',{'stds':stds,'mediums':mediums})

@is_authenticated
@is_teacher
def t_saveresult(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed..!")
    else :
        try :
            title = request.POST.get('title')
            medium = request.POST.get('medium')
            std = request.POST.get('std')
            resultfile = request.FILES['resultfile']
            created_by = request.user.username

            result = Result.objects.create(title=title,file=resultfile,medium=medium,std=std,created_by=created_by)
            result.save()
            
            messages.success(request,"Result uploaded successfully")
            return HttpResponseRedirect("/t_addresult")
        except :
            messages.error(request,"Failed to upload result")
            return HttpResponseRedirect("/t_addresult")

@is_authenticated
@is_teacher
def t_deleteresult(request):
    try: 
        results = Result.objects.filter(created_by=request.user.username)
        return render(request,'teacher/t_deleteresult.html',{'results':results})
    except:
        return render(request,'teacher/t_deleteresult.html')

@is_authenticated
@is_teacher
def t_removeresult(request,result_id):
    result = Result.objects.get(id=result_id)
    try:
        result.file.delete()
        result.delete()
        messages.success(request,"result deleted successfully")
        return HttpResponseRedirect("/t_deleteresult")
    except :
        messages.error(request,"Failed to delete result")
        return HttpResponseRedirect("/t_deleteresult")

@is_authenticated
@is_teacher
def t_viewresult(request):
    results = Result.objects.all()
    return render(request,'teacher/t_viewresult.html',{'results':results})

@is_authenticated
@is_teacher
def t_addnotes(request):
    stds = Result.std_choices
    mediums = Result.medium_choices
    return render(request,'teacher/t_addnotes.html',{'stds':stds,'mediums':mediums})

@is_authenticated
@is_teacher
def t_savenotes(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed..!")
    else :
        try :
            title = request.POST.get('title')
            medium = request.POST.get('medium')
            std = request.POST.get('std')
            file = request.FILES['notes']
            created_by = request.user.username

            notes = Notes.objects.create(title=title,file=file,medium=medium,std=std,created_by=created_by)
            notes.save()
            
            messages.success(request,"Notes uploaded successfully")
            return HttpResponseRedirect("/t_addnotes")
        except :
            messages.error(request,"Failed to upload Notes")
            return HttpResponseRedirect("/t_addnotes")

@is_authenticated
@is_teacher
def t_deletenotes(request):
    try: 
        notes = Notes.objects.filter(created_by=request.user.username)
        return render(request,'teacher/t_deletenotes.html',{'notes':notes})
    except:
        return render(request,'teacher/t_deletenotes.html')

@is_authenticated
@is_teacher
def t_removenotes(request,notes_id):
    notes = Notes.objects.get(id=notes_id)
    try:
        notes.file.delete()
        notes.delete()
        messages.success(request,"Note deleted successfully")
        return HttpResponseRedirect("/t_deletenotes")
    except :
        messages.error(request,"Failed to delete Note")
        return HttpResponseRedirect("/t_deletenotes")

@is_authenticated
@is_teacher
def t_viewnotes(request):
    notes = Notes.objects.all()
    return render(request,'teacher/t_viewnotes.html',{'notes':notes})
