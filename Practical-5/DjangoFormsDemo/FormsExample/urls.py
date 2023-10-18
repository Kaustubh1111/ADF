from django import views
from django.urls import path
from .views import *
from FormsExample import views

urlpatterns = [
    path('', views.home_view),
    
]