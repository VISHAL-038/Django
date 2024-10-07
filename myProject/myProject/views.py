from django.http import HttpResponse
from django.http import HttpResponseRedirect 
from django.shortcuts import render
from .forms import userForms 
# from .forms import <name of the function created in the page forms.py>

# model
from service.models import Service
from news.models import News

#pagination
from django.core.paginator import Paginator

def indexPage(request):
    servicesData = Service.objects.all()[:3] #negative index not supported
    newsData=News.objects.all()
    print(servicesData)
    data = {
         'servicesData': servicesData,
         'newsData':newsData
    }
    return render(request,'index.html',data)

def newsDetails(request,slug):
     newsDetails = News.objects.get(news_slug=slug)
     data = {
          'newsDetails': newsDetails
     }
     return render(request,'newsDetails.html',data)

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
     # servicesData = Service.objects.all().order_by('service_title') assending order 
     # servicesData = Service.objects.all().order_by('-service_title')  desending order
     servicesData = Service.objects.all()
     # paginator
     # paginator = Paginator(servicesData,3)
     # page_number = request.GET.get('page')
     # servicesDataFinal = paginator.get_page(page_number)
     # page_obj = paginator.get_page(page_number)
     if request.method=="GET":
          st = request.GET.get('servicename')
          if st!=None:
               # servicesData = Service.objects.filter(service_title=st) have to write complete name 
               servicesData = Service.objects.filter(service_title__icontains=st)  # this will work same as like keyword in database
     print(servicesData)
     data = {
         'servicesData': servicesData
     }
     return render(request,'services.html',data)

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

def evenodd(request):
     c=''
     try:
          if request.method=="POST":
               if request.POST.get('num1')=="":
                    return render(request,'evenodd.html',{'error':True})
               n1 = eval(request.POST.get('num1'))
               if n1%2==0:
                    c="even number"
               else:
                    c="odd number"
     except:
          c="Invalid entry...."
     return render(request,'evenodd.html',{'c':c})

def marksheet(request):
     total = 0
     percentage = 0
     grade = ''
     data={}
     try:
          if request.method=="POST":
               m1 = eval(request.POST.get('num1'))
               m2 = eval(request.POST.get('num1'))
               m3 = eval(request.POST.get('num1'))
               m4 = eval(request.POST.get('num1'))
               m5 = eval(request.POST.get('num1'))
               total = m1+m2+m3+m4+m5
               percentage = (total/500)*100
               if percentage>=90:
                    grade='A'
               elif percentage>=80:
                    grade='B'
               elif percentage>=70:
                    grade='C'
               elif percentage>=60:
                    grade='D'
               else:
                    grade='F'
               data = {
                    'total':total,
                    'percentage':percentage,
                    'grade':grade
               }
               print(grade)
     except:
          pass
     return render(request,'marksheet.html',data)


# def Courses(request):
#     return HttpResponse("Welcome to Django Python Courses")

# def courseDetails(request,courseid):
#     return HttpResponse(courseid)