"""
URL configuration for myProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from myProject import forms,views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('aboutus/', views.aboutUS),
    path('contact/', views.contact),
    path('services/', views.services,name="services"),
    path('book/', views.book,name="book"),
    path('userform/', views.userform,name="userform"),
    path('formuser/', views.formuser,name="formuser"),
    path('submitform/', views.submitform,name="submitform"),
    path('', views.indexPage),
    path('calculator/', views.calculator),
    path('saveenquiry/', views.saveEnquiry,name='saveenquiry'),
    path('evenodd/', views.evenodd),
    path('marksheet/', views.marksheet),
    path('newsdetails/<slug>', views.newsDetails),
    # path('course/', views.Courses),
    # path('course/<courseid>', views.courseDetails),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)