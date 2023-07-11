from django import forms


class StudentRegistations(forms.Form):
    name=forms.CharField(max_length=50)
    email=forms.EmailField(max_length=50)
    password=forms.CharField(widget=forms.PasswordInput())