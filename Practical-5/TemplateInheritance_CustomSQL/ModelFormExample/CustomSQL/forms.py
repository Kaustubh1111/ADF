from django import forms  

class InputForm(forms.Form):
    first_name = forms.CharField(max_length=20)  
    last_name  = forms.CharField(max_length=30)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':3})) 
    email_id= forms.EmailField()
    age = forms.IntegerField()
    agree = forms.BooleanField()