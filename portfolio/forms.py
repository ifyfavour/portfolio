from django import forms
from .models import Service, PortfolioImage

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description']

class PortfolioImageForm(forms.ModelForm):
    class Meta:
        model = PortfolioImage
        fields = ['image', 'description']
