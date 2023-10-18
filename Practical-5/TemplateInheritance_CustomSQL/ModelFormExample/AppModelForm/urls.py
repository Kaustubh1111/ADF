from django.contrib import admin  
from django.urls import path  
from AppModelForm import views  
urlpatterns = [    
    path('', views.index),  
]  