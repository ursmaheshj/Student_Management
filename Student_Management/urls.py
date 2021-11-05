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
    path('adminhome/', v_admin.a_home),
    path('addteacher/',v_admin.addteacher,name='addteacher'),
    path('saveteacher',v_admin.saveteacher),
    path('addstudent/',v_admin.addstudent,name='addstudent'),
    path('savestudent',v_admin.savestudent),
    path('manageteacher',v_admin.manageteacher,name='manageteacher'),
    path('managestudent',v_admin.managestudent,name='managestudent'),


    #Teacher URL's


    #Student URL's


]
