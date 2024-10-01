from django.http import HttpResponse
from django.shortcuts import render

def indexPage(request):
    return render(request,'index.html')

# def homePage(request):
#     data={
#         'title':'Home Page !',
#         'message':'Welcome to my home page',
#         'clist':['PHP','Java','Django'],
#         'numbers':[10,20,30,40,50],
#         'student_details':[
#             {'name':'person_1','phone':123456789},
#             {'name':'person_2','phone':987654321},
#         ]
#     } 
#     return render(request,'main.html',data)

# def aboutUS(request):
#     return HttpResponse("Welcome to Django Python")

def aboutUS(request):
     return render(request,'aboutus.html')

def contact(request):
     return render(request,'contact.html')

def services(request):
     return render(request,'services.html')

def Courses(request):
    return HttpResponse("Welcome to Django Python Courses")

def courseDetails(request,courseid):
    return HttpResponse(courseid)