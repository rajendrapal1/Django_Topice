from django import forms


class ContectForm(forms.Form):
    name=forms.CharField(max_length=40)
    email=forms.EmailField(max_length=30)
    ms=forms.CharField(widget=forms.Textarea())
    