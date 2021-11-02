from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def t_home(request):
    return render(request,'teacher/t_home.html')
