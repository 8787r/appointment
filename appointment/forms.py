from django import forms
from .models import *

class appointForm(forms.Form):
    name_patient = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Please enter patient name.'}), label='Patient Name')
    contact_no = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Please enter contact number.'}), label='Contact Number')
    date = forms.DateTimeField()
    name_doctor = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Please enter doctor name.'}), label='Doctor Name')

    class Meta:
        model = Registration
        fields = ('name_patient', 'contact_no', 'date', 'name_doctor')