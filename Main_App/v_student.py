from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def s_home(request):
    return render(request,'student/s_home.html')
