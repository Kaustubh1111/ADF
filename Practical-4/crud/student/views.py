from django.shortcuts import render, HttpResponseRedirect
from .forms import studentForm
from .models import studentDetails

# Create your views here.

def stu(req):
    if req.method == "POST":
        form = studentForm(req.POST)
        if(form.is_valid()):
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = studentForm()
    
    return render(req,'index.html',{'form':form})

def show(req):
    students = studentDetails.objects.all()
    return render(req,"show.html",{'students':students})

