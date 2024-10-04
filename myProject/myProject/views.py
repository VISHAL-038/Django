from django.http import HttpResponse
from django.http import HttpResponseRedirect 
from django.shortcuts import render
from .forms import userForms 
# from .forms import <name of the function created in the page forms.py>

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
     if request.method=="GET":
          output = request.GET.get('output')
     return render(request,'aboutus.html',{'output':output})

def contact(request):
     return render(request,'contact.html')

def services(request):
     return render(request,'services.html')

def book(request):
     return render(request,'book.html')


# def userform(request):
#      finalans= 0
#      data={}
#      try:
#           # n1 = int(request.GET['num1'])
#           # n2 = int(request.GET['num2'])
#           n1 = request.GET.get('num1')
#           n2 = request.GET.get('num2')
#           finalans=n1+n2
#           data = {
#                'n1':n1,
#                'n2':n2,
#                'output':finalans
#           }
#      except:
#           pass
#      return render(request,'userform.html',data)

def userform(request):
     finalans = 0
     fn = userForms()
     data={'form':fn}
     try:
          if request.method=="POST":
               n1 = request.POST.get('num1')
               n2 = request.POST.get('num2')
               finalans = n1+n2
               data={
                    'form':fn,
                    'output':finalans,
               }
               url ="/aboutus/?output={}".format(finalans)
               return HttpResponseRedirect(url)
     except:
          pass
     return render(request,'userform.html',data)

def formuser(request):
     finalans = 0
     try:
          if request.method=="POST":
               n1 = request.POST.get('num1')
               n2 = request.POST.get('num2')
               finalans = n1+n2
               url ="/aboutus/?output={}".format(finalans)
               return HttpResponseRedirect(url)
     except:
          pass
     return render(request,'formuser.html',{'output':finalans})

def submitform(request):
     # return HttpResponse(request)
     # return render(request,'submit.html')
     finalans= 0
     data={}
     try:
          # n1 = int(request.GET['num1'])
          # n2 = int(request.GET['num2'])
          n1 = request.GET.get('num1')
          n2 = request.GET.get('num2')
          finalans=n1+n2
          data = {
               'n1':n1,
               'n2':n2,
               'output':finalans
          }
     except:
          pass
     return render(request,'submit.html',data)


def calculator(request):
     c=''
     try:
          if request.method=="POST":
               n1 = eval(request.POST.get('num1'))
               n2 = eval(request.POST.get('num2'))
               opr = request.POST.get('opr')
               if opr=="+":
                    c=n1+n2
               elif opr=="-":
                    c=n1-n2
               elif opr=="*":
                    c=n1*n2
               elif opr=='/':
                    c=n1/n2
               

     except:
          c="invalid operation......"
     print(c)
     return render(request,'calculator.html',{'c':c})


# def Courses(request):
#     return HttpResponse("Welcome to Django Python Courses")

# def courseDetails(request,courseid):
#     return HttpResponse(courseid)