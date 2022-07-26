from pyexpat import model
from django import forms
from .models import User_service

class AddService(forms.ModelForm):
    class Meta:
        model = User_service
        fields = ['name', 'service', 'date', 'check_in', 'check_out', 'service_man', 'cost']
        widgets = {
            'date' : forms.DateInput(attrs={'class' : 'form-control'}),
            'check_in' : forms.DateTimeInput(attrs={'class' : 'form-control'}),
            'check_out' : forms.DateTimeInput(attrs={'class' : 'form-control'}),
        }