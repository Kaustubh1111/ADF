from django import forms
from .models import studenttable

class misform(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = studenttable()
        fields = "__all__"

    