from django import forms
from .models import Health


class HealthForm(forms.ModelForm):
    class Meta:
        model = Health
        fields = ('systolic_blood_pressure', 'diastolic_blood_pressure', 'pulse', 'glucose', 'comment')
