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
    path('', views.loginpage),
    path('loginuser',views.loginuser),
    path('logoutuser',views.logoutuser),

    #Admin URL's
    path('adminhome/', v_admin.a_home,name='adminhome'),
    path('adminprofile/',v_admin.adminprofile,name='adminprofile'),
    path('addteacher/',v_admin.addteacher,name='addteacher'),
    path('saveteacher',v_admin.saveteacher),
    path('addstudent/',v_admin.addstudent,name='addstudent'),
    path('savestudent',v_admin.savestudent),
    path('manageteacher/',v_admin.manageteacher,name='manageteacher'),
    path('deleteteacher/<int:teacher_id>',v_admin.deleteteacher),
    path('resetteacherpass/<int:teacher_id>',v_admin.resetteacherpass),
    path('managestudent/',v_admin.managestudent,name='managestudent'),
    path('deletestudent/<int:student_id>',v_admin.deletestudent),
    path('resetstudentpass/<int:student_id>',v_admin.resetstudentpass),
    path('editteacher/<int:teacher_id>',v_admin.editteacher,name='editteacher'),
    path('saveeditteacher',v_admin.saveeditteacher),
    path('editstudent/<int:student_id>',v_admin.editstudent,name='editstudent'),
    path('saveeditstudent',v_admin.saveeditstudent),
    path('a_addnotification/',v_admin.a_addnotification,name="a_addnotification"),
    path('a_savenotification',v_admin.a_savenotification),
    path('managenotification/',v_admin.managenotification,name='managenotification'),
    path('a_deletenotification/<int:notification_id>',v_admin.a_deletenotification,name='deletenotification'),
    path('a_addresult/',v_admin.a_addresult),
    path('a_saveresult',v_admin.a_saveresult),
    path('a_viewresult/',v_admin.a_viewresult),
    path('a_removeresult/<int:result_id>',v_admin.a_removeresult),
    path('a_addnotes/',v_admin.a_addnotes),
    path('a_savenotes',v_admin.a_savenotes),
    path('a_viewnotes/',v_admin.a_viewnotes),
    path('a_removenotes/<int:notes_id>',v_admin.a_removenotes),

    #Teacher URL's
    path('teacherhome/', v_teacher.t_home),
    path('teacherprofile/',v_teacher.t_profile),
    path('t_saveprofile',v_teacher.t_saveprofile),
    path('t_addstudent/', v_teacher.t_addstudent),
    path('t_savestudent',v_teacher.t_savestudent),
    path('t_viewstudent/', v_teacher.t_viewstudent),
    path('t_resetspass/<int:student_id>', v_teacher.t_resetspass),
    path('t_addnotification/', v_teacher.t_addnotification),
    path('t_savenotification',v_teacher.t_savenotification),
    path('t_deletenotification/',v_teacher.t_deletenotification),
    path('t_removenotification/<int:notification_id>',v_teacher.t_removenotification),
    path('t_viewnotification/',v_teacher.t_viewnotification),
    path('t_addresult/',v_teacher.t_addresult),
    path('t_saveresult',v_teacher.t_saveresult),
    path('t_deleteresult/',v_teacher.t_deleteresult),
    path('t_removeresult/<int:result_id>',v_teacher.t_removeresult),
    path('t_viewresult/',v_teacher.t_viewresult),
    path('t_addnotes/',v_teacher.t_addnotes),
    path('t_savenotes',v_teacher.t_savenotes),
    path('t_deletenotes/',v_teacher.t_deletenotes),
    path('t_removenotes/<int:notes_id>',v_teacher.t_removenotes),
    path('t_viewnotes/',v_teacher.t_viewnotes),

    #Student URL's
    path('studenthome/', v_student.s_home),
    path('studentprofile/',v_student.s_profile),
    path('s_saveprofile',v_student.s_saveprofile),
    path('s_viewresult/',v_student.s_viewresult),
    path('s_viewnotification/',v_student.s_viewnotification),
    path('s_viewnotes/', v_student.s_viewnotes),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
