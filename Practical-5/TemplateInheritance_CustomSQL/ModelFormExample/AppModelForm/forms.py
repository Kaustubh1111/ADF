from django import forms  
from AppModelForm.models import Student  
  
class EmpForm(forms.ModelForm): 

    class Meta:  
        model = Student  
        fields = "__all__" 
        #fields = ['first_name','last_name','description','email_id','age','agree']
