from app1.models import School
from django import forms


class Schoolform(forms.ModelForm):
    location_choices=[('ernakulam','ernakulam'),('trivandrum','trivandrum'),('kollam','kollam')]
    location=forms.ChoiceField(choices=location_choices,widget=forms.Select,required=True)
    class Meta:
        model=School
        fields=['name','location','principal']

from django.contrib.auth.models import User
class Password(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']

