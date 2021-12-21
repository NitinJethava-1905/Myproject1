from django import forms
from django.forms import fields
from .models import SignupMaster, careermaster, inquirymaster

class SignupForm(forms.ModelForm):
    class Meta:
        model=SignupMaster
        fields="__all__"
    
class CareerForm(forms.ModelForm):
    class Meta:
        model=careermaster
        fields="__all__"
    
class InquiryForm(forms.ModelForm):
    class Meta:
        model=inquirymaster
        fields="__all__"
