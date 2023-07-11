from django import forms

class forms_class(forms.Form):
    name=forms.CharField(label='Enter a name',max_length=50)
    email=forms.EmailField(label="Enter a email",max_length=50)
    password = forms.CharField(label="Enter a password",widget=forms.PasswordInput())
