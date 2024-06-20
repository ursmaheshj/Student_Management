#from django.contrib.auth import authenticate,login,logout
from django.contrib import admin, messages
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from random import randint
from datetime import date

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from Main_App.restrictions import is_admin, is_authenticated
from Main_App.models import MyUser, Notes, Notification, Result,Teacher, Student


# Create your views here.
@is_authenticated
@is_admin
def a_home(request):

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

    return render(request,'admin/a_home.html',context)

@is_authenticated
@is_admin
def adminprofile(request):
    return render(request,'admin/a_profile.html')
   
@is_authenticated
@is_admin 
def addteacher(request):
    genders = Teacher.gender_choices
    return render(request,'admin/a_addteacher.html',{'genders':genders})

@is_authenticated
@is_admin
def saveteacher(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed..!")
    else :
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        password = "Teacher@100"

        def random_username():
            r=randint(1000,9999)
            
            username = "TC"+str(date.today().year)+str(r)
            
            try:
                Teacher.objects.get(username=username)
                return random_username()
            except :
                return username;

        try :
            username = random_username()
            user = MyUser.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname,user_type=2)
            user.teacher.address=address
            user.teacher.gender=gender        
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

            messages.success(request,"Teacher added successfully")
            return HttpResponseRedirect("/addteacher")
        except :
            messages.error(request,"Failed to add teacher")
            return HttpResponseRedirect("/addteacher")

@is_authenticated
@is_admin
def manageteacher(request):
    teachers = Teacher.objects.all()
    return render(request,'admin/a_manageteacher.html',{'teachers':teachers})

@is_authenticated
@is_admin
def deleteteacher(request,teacher_id):
    try:
        customuser = MyUser.objects.get(id=teacher_id)
        customuser.delete()
        messages.success(request,"Teacher deleted successfully")
        return HttpResponseRedirect("/manageteacher")
    except :
        messages.error(request,"Failed to delete Teacher")
        return HttpResponseRedirect("/manageteacher")

@is_authenticated
@is_admin
def resetteacherpass(request,teacher_id):
    try:
        password = "Teacher@100"
        user = MyUser.objects.get(id=teacher_id)
        
        user.set_password(password)
        user.save()
        messages.success(request,"Password reset successfully to Teacher@100")
        return HttpResponseRedirect("/manageteacher")
    except :
        messages.error(request,"Failed to reset password")
        return HttpResponseRedirect("/manageteacher")

@is_authenticated
@is_admin
def editteacher(request,teacher_id):
    teacher = Teacher.objects.get(admin=teacher_id)
    return render(request,'admin/a_editteacher.html',{'teacher':teacher})

@is_authenticated
@is_admin
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


@is_authenticated
@is_admin
def addstudent(request):
    genders = Student.gender_choices
    stds = Student.std_choices
    mediums = Student.medium_choices
    return render(request,'admin/a_addstudent.html',{'genders':genders,'stds':stds,'mediums':mediums})

@is_authenticated
@is_admin
def savestudent(request):
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
        #     'Kagne Coaching account creation!',
        #     template,
        #     settings.EMAIL_HOST_USER,
        #     [email]
        # ) 
        # email.fail_silently = False
        # email.send()

        messages.success(request,"Student added successfully")
        return HttpResponseRedirect("/addstudent")
    except :
        messages.error(request,"Failed to add student")
        return HttpResponseRedirect("/addstudent")


@is_authenticated
@is_admin
def managestudent(request):
    students = Student.objects.all()
    return render(request,'admin/a_managestudent.html',{'students':students})

@is_authenticated
@is_admin
def deletestudent(request,student_id):
    try:    
        customuser = MyUser.objects.get(id=student_id)
        customuser.delete()
        messages.success(request,"Student deleted successfully")
        return HttpResponseRedirect("/managestudent")
    except :
        messages.error(request,"Failed to delete Student")
        return HttpResponseRedirect("/managestudent")

@is_authenticated
@is_admin
def resetstudentpass(request,student_id):
    try:
        password = "Student@100"
        user = MyUser.objects.get(id=student_id)
        user.set_password(password)
        user.save()
        messages.success(request,"Password reset successfully to Student@100")
        return HttpResponseRedirect("/managestudent")
    except :
        messages.error(request,"Failed to reset password")
        return HttpResponseRedirect("/managestudent")

@is_authenticated
@is_admin
def editstudent(request,student_id):
    student = Student.objects.get(admin=student_id)
    return render(request,'admin/a_editstudent.html',{'student':student})

@is_authenticated
@is_admin
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

@is_authenticated
@is_admin
def a_addnotification(request):
    return render(request,'admin/a_addnotification.html')

@is_authenticated
@is_admin
def a_savenotification(request):
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
            return HttpResponseRedirect("/a_addnotification")
        except :
            messages.error(request,"Failed to add Notification")
            return HttpResponseRedirect("/a_addnotification")

@is_authenticated
@is_admin
def managenotification(request):
    notifications = Notification.objects.all()
    return render(request,'admin/a_managenotification.html',{'notifications':notifications})

@is_authenticated
@is_admin
def a_deletenotification(request,notification_id):
    notification = Notification.objects.get(id=notification_id)
    try:
        notification.delete()
        messages.success(request,"Notification deleted successfully")
        return HttpResponseRedirect("/managenotification")
    except :
        messages.error(request,"Failed to delete Notification")
        return HttpResponseRedirect("/managenotification")

@is_authenticated
@is_admin
def a_addresult(request):
    stds = Result.std_choices
    mediums = Result.medium_choices
    return render(request,'admin/a_addresult.html',{'stds':stds,'mediums':mediums})

@is_authenticated
@is_admin
def a_saveresult(request):
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
            return HttpResponseRedirect("/a_addresult")
        except :
            messages.error(request,"Failed to upload result")
            return HttpResponseRedirect("/a_addresult")

@is_authenticated
@is_admin
def a_viewresult(request):
    results = Result.objects.all()
    return render(request,'admin/a_viewresult.html',{'results':results})

@is_authenticated
@is_admin
def a_removeresult(request,result_id):
    result = Result.objects.get(id=result_id)
    try:
        result.file.delete()
        result.delete()
        messages.success(request,"Result deleted successfully")
        return HttpResponseRedirect("/a_viewresult")
    except :
        messages.error(request,"Failed to delete result")
        return HttpResponseRedirect("/a_viewresult")

@is_authenticated
@is_admin
def a_addnotes(request):
    stds = Result.std_choices
    mediums = Result.medium_choices
    return render(request,'admin/a_addnotes.html',{'stds':stds,'mediums':mediums})

@is_authenticated
@is_admin
def a_savenotes(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed..!")
    else :
        try :
            title = request.POST.get('title')
            medium = request.POST.get('medium')
            std = request.POST.get('std')
            notesfile = request.FILES['notesfile']
            created_by = request.user.username

            note = Notes.objects.create(title=title,file=notesfile,medium=medium,std=std,created_by=created_by)
            note.save()
            
            messages.success(request,"Notes uploaded successfully")
            return HttpResponseRedirect("/a_addnotes")
        except :
            messages.error(request,"Failed to upload notes")
            return HttpResponseRedirect("/a_addnotes")

@is_authenticated
@is_admin
def a_viewnotes(request):
    notes = Notes.objects.all()
    return render(request,'admin/a_viewnotes.html',{'notes':notes})

@is_authenticated
@is_admin
def a_removenotes(request,notes_id):
    notes = Notes.objects.get(id=notes_id)
    try:
        notes.file.delete()
        notes.delete()
        messages.success(request,"Note deleted successfully")
        return HttpResponseRedirect("/a_viewnotes")
    except :
        messages.error(request,"Failed to delete note")
        return HttpResponseRedirect("/a_viewnotes")