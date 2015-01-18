from django import forms

from .models import Institution

class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
    
