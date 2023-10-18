from django.shortcuts import render, redirect
from .form import misform
# Create your views here.
def create_view(req):
    if req.method == "POST":
        form = misform(req.POST)

        if form.is_valid():
            form.save()
    else:
        form = misform()

    return render(req,'index.html',{'form': form})