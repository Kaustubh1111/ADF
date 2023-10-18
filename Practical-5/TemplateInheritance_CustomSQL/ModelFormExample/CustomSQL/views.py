from django.shortcuts import render,redirect
from CustomSQL.forms import InputForm
from django.db import connection
import datetime
# Create your views here.
def cindex(request):
    if request.method == "POST": 
            iform = InputForm(request.POST)
            dt= datetime.datetime.now()
            if request.POST['agree']=="on":
                 cb=1
            else:
                 cb=0
            #print(cb)
            #print("Checkbox:") 
            #print(request.POST['agree'])
            if iform.is_valid():    
                with connection.cursor() as cursor:

                    cursor.execute("insert into AppModelForm_Student(first_name,last_name,description,last_modified,email_id,age,agree) values(%s,%s,%s,%s,%s,%s,%s)", 
                                   [
                                        request.POST['first_name'],
                                        request.POST['last_name'],
                                        request.POST['description'],
                                        dt,
                                        request.POST['email_id'],
                                        request.POST['age'],
                                        cb
                                    ])

                return redirect('.')
    else:
        inputform=InputForm()
        return render(request,"cindex.html",{'form':inputform})
