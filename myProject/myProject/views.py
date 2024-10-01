from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    return render(request,'index.html')

def aboutUS(request):
    return HttpResponse("Welcome to Django Python")

def Courses(request):
    return HttpResponse("Welcome to Django Python Courses")

def courseDetails(request,courseid):
    return HttpResponse(courseid)