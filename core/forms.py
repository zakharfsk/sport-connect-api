from django import forms

from users.models import Schools


class GetFileForStudentCalculationForm(forms.Form):
    school_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )
    school_class = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )
