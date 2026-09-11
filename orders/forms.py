from django import forms

from .models import ReferenceImage, LogoOrder

class ReferenceImageForms(forms.ModelForm):
    class Meta:
        model = ReferenceImage
        fields = [
            'image',
            'url',
        ]


class LogoOrderForms(forms.ModelForm):
    class Meta:
        model = LogoOrder
        fields = [
            'name',
            'style',
            'personality',
            'color_preferences',
            'usage',
            'brief_text',
            'budget',
            'deadline',
            'references',
        ]
