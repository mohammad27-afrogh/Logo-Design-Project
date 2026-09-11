from django import forms

from .models import PortfolioItem, PortfolioImage

class PortfolioItemForms(forms.ModelForm):
    class Meta:
        model = PortfolioItem
        fields = [
            'title',
            'slug',
            'style',
            'personality',
            'description',
            'is_featured',
            'created_at',
        ]

class PortfolioImage(forms.ModelForm):
    class Meta:
        model = PortfolioImage
        fields = [
            'project',
            'image',
        ]