from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from Main_App.models import MyUser,Admin,Teacher,Student,Notification

class UserModel(UserAdmin):
    pass

# Register your models here.
admin.register(MyUser,UserModel)
admin.register(Admin)
admin.register(Teacher)
admin.register(Student)
admin.register(Notification)