from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from Main_App.models import MyUser, Notes, Notification, Result, Student
from Main_App.restrictions import is_authenticated, is_student

@is_authenticated
@is_student
def s_home(request):
    marathi_count = Student.objects.filter(medium='Marathi').count()
    semi_count = Student.objects.filter(medium='SemiEng').count()
    cbse_count = Student.objects.filter(medium='CBSE').count()
    foundation_count = Student.objects.filter(medium='Foundation').count()

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

    return render(request,'student/s_home.html',context)

@is_authenticated
@is_student
def s_profile(request):
    return render(request,'student/s_profile.html')

@is_authenticated
@is_student
def s_saveprofile(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed..!")
    else :
        student_id = request.POST.get('student_id')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        try :
            user = MyUser.objects.get(id=student_id)
            user.first_name=firstname
            user.last_name=lastname
            user.email=email  
            if password != None and password != "":
                user.set_password(password)
            user.save()

            student = Student.objects.get(admin=student_id)
            student.address=address
            student.gender=gender  
            student.save()
            messages.success(request,"Profile updated successfully")
            return HttpResponseRedirect('/studentprofile')
        except :
            messages.error(request,"Failed to update profile")
            return HttpResponseRedirect('/studentprofile')

@is_authenticated
@is_student
def s_viewresult(request):
    try:
        s = Student.objects.get(admin=request.user.id)
        results = Result.objects.filter(std=s.std,medium=s.medium)
        return render(request,'student/s_viewresult.html',{'results':results})
    except:
        return HttpResponse('<h1>You need to login first</h1>')

@is_authenticated
@is_student
def s_viewnotification(request):
    notifications = Notification.objects.all()
    return render(request,'student/s_viewnotification.html',{'notifications':notifications})

@is_authenticated
@is_student
def s_viewnotes(request):
    try:
        s = Student.objects.get(admin=request.user.id)
        notes = Notes.objects.filter(std=s.std,medium=s.medium)
        return render(request,'student/s_viewnotes.html',{'notes':notes})
    except:
        return HttpResponse('<h1>You need to login first</h1>')