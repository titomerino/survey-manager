from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "last_name", "NIE", "state"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "NIE": forms.TextInput(attrs={"class": "form-control"}),
            "state": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
