from django.contrib import admin  
from django.urls import path  
from TemplateDemo import views  
urlpatterns = [    
    path('',views.tindex),  
]  