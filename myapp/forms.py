
'''from django import forms
from .models import student

class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ["name", "email", "age"]'''



from django.http import forms
from .models import student

class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ["name", "email", "age"]