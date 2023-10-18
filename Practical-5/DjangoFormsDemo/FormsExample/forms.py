# import the standard Django Forms
# from built-in library
from django import forms
	
# creating a form
class InputForm(forms.Form):
	
	first_name = forms.CharField(max_length = 200)
	last_name = forms.CharField(max_length = 200, required=False)
	roll_number = forms.IntegerField(
					help_text = "Enter 6 digit roll number"
					)
	password = forms.CharField(widget = forms.PasswordInput())
 
# A widget is Django's representation of an HTML input element. 
# The widget handles the rendering of the HTML, and the extraction of data from a 
# GET/POST dictionary that corresponds to the widget. 