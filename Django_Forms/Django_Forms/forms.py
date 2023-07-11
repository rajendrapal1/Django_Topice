from django import forms

class forms_class(forms.Form):
    name=forms.CharField(max_length=50)
    email=forms.EmailField(max_length=50)
    submit=forms.CharField(max_length=40)