from django.contrib import admin  
from django.urls import path  
from CustomSQL import views  
urlpatterns = [    
    path('',views.cindex ),  
]  