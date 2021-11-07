"""Student_Management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Student_Management import settings
from django.conf.urls.static import static

from Main_App import views,v_admin,v_student,v_teacher

urlpatterns = [
    #Common URL's
    path('admin/', admin.site.urls),
    path('', views.index),
    path('loginpage/', views.loginpage),
    path('loginuser',views.loginuser),
    path('logoutuser',views.logoutuser),

    #Admin URL's
    path('adminhome/', v_admin.a_home,name='adminhome'),
    path('addteacher/',v_admin.addteacher,name='addteacher'),
    path('saveteacher',v_admin.saveteacher),
    path('addstudent/',v_admin.addstudent,name='addstudent'),
    path('savestudent',v_admin.savestudent),
    path('manageteacher/',v_admin.manageteacher,name='manageteacher'),
    path('managestudent/',v_admin.managestudent,name='managestudent'),
    path('editteacher/<int:teacher_id>',v_admin.editteacher,name='editteacher'),
    path('saveeditteacher',v_admin.saveeditteacher),
    path('editstudent/<int:student_id>',v_admin.editstudent,name='editstudent'),
    path('saveeditstudent',v_admin.saveeditstudent),
    path('a_addnotification/',v_admin.a_addnotification,name="a_addnotification"),
    path('savenotification',v_admin.savenotification),
    path('managenotification/',v_admin.managenotification,name='managenotification'),

    #Teacher URL's
    path('teacherhome/', v_teacher.t_home),
    #path('t_addstudent/', v_teacher.t_addstudent),
    #path('viewstudent/', v_teacher.viewstudent),
    #path('t_addnotification/', v_teacher.t_addnotification),

    
    #Student URL's
    path('studenthome/', v_student.s_home)

    

]#+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
