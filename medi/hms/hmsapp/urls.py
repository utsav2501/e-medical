from django.http import HttpResponse
from . import views
from django.urls import path
from . views import *

from django.contrib import admin

urlpatterns = [
    path('home/',views.home,name = "home"),
    path('process_patient_entry/',views.process_patient_entry,name = "process_patient_entry"),
    path('', index, name="index"),
    path('index/booking', booking, name="booking"),
    path('registation/', registation, name="registation"),
    path('signup/', views.handlesignup, name="handlesignup"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
]