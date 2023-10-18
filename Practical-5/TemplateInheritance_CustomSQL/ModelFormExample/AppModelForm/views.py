from django.shortcuts import render,redirect

# Create your views here.

from AppModelForm.forms import EmpForm
  
def index(request):
    if request.method == "POST": 
        emp = EmpForm(request.POST)
        if emp.is_valid():
            emp.save()  
            return redirect('.')
    else:
        emp = EmpForm()
    return render(request,"index.html",{'form':emp})  