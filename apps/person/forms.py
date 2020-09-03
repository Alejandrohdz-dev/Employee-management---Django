from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    """Form definition for Employee."""

    class Meta:
        """Meta definition for Employeeform."""

        model = Employee
        fields = (
            'first_name',
            'last_name',
            'job',
            'department',
            'avatar',
            'skills',
        )

        widgets = {
            'skills': forms.CheckboxSelectMultiple()
        }