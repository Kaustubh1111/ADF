from django.shortcuts import render

# Create your views here.
#from .forms import InputForm

from FormsExample.forms import InputForm
# Create your views here.
def home_view(request):
    inputform = InputForm()
    return render(request, "home.html", {'form':inputform})