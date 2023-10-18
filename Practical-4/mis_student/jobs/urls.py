"""mis_student URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('custom_job_posting/', views.custom_job_posting, name='custom_job_posting'),
    path('add/', views.add_salary, name='add_salary'),
    path('decrease/', views.dec_salary, name='dec_salary'),
    path('job_postings/', views.job_postings, name='job_postings'),
    path('create_job_posting/', views.create_job_posting, name='create_job_posting'),
    path('job_posting/<int:job_posting_id>/', views.job_posting_detail, name='job_posting_detail'),
    path('job_postings/delete/<int:job_posting_id>/', views.delete_job_posting, name='delete_job_posting'),
]
