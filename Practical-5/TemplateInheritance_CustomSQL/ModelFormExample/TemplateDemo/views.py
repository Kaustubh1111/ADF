from django.shortcuts import render

# Create your views here.

def tindex(request):
    return render(request,"tdemo.html")