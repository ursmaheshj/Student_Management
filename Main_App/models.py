from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class MyUser(AbstractUser):
    user_types = ((1,'Admin'),(2,'Teacher'),(3,'Student'))
    user_type = models.CharField(default=1,choices=user_types,max_length=10)

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(MyUser,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    objects = models.Manager()

class Teacher(models.Model):
    gender_choices = (('Male','Male'),('Female','Female'),('Other','Other'))
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(MyUser,on_delete=models.CASCADE)
    gender = models.CharField(max_length=15,choices=gender_choices,default='Other')
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Student(models.Model):
    medium_choices = (('Marathi','Marathi'),('Semi Eng','Semi Eng'),('CBSE','CBSE'))
    gender_choices = (('Male','Male'),('Female','Female'),('Other','Other'))
    std_choices = ((1,1),(2,2),(3,3),(4,4),(5,5),(6,6))
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(MyUser,on_delete=models.CASCADE)
    gender = models.CharField(max_length=15,choices=gender_choices,default='Other')
    std = models.CharField(max_length=10,choices=std_choices)
    medium = models.CharField(max_length=15 ,choices=medium_choices, default='Marathi')
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


@receiver(post_save,sender=MyUser)
def user_create(sender,instance,created,**kwargs):
    if created:
        if instance.user_type == 1:
            Admin.objects.create(admin=instance)
        if instance.user_type == 2:
            Teacher.objects.create(admin=instance)
        if instance.user_type == 3:
            Student.objects.create(admin=instance)

@receiver(post_save,sender=MyUser)
def user_save(sender,instance,**kwargs):
        if instance.user_type == 1:
            instance.admin.save()
        if instance.user_type == 2:
            instance.teacher.save()
        if instance.user_type == 3:
            instance.student.save()