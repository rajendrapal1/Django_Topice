from django import forms
from app_models.models import Model_Forms

class Studen_Registations(forms.ModelForm):
    class Meta:
        model = Model_Forms
        # fields = ["name", "email", "password",]
        fields = '__all__'
