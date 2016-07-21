from django import forms
from visit.models import Visitor
class VisitorForm(forms.ModelForm): 
	name = forms.CharField(max_length=100, help_text="Please enter the name.") 
	age=forms.IntegerField(help_text="Enter Age")
	mobile_no=forms.IntegerField(max_length=10,help_text="Enter Mobile Number")
	company=forms.CharField(max_length=100,help_text="Enter Your company name")
	visiting=forms.CharField(max_length=100,help_text="Enter the name of company to visit")
	
# An inline class to provide additional information on the form. 
class Meta: # Provide an association between the ModelForm and a model 
  model = Visitor
