from django import forms

from .models import AboutUs, Privacy

class AboutUsForms(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = [
            'title',
            'discription',
        ]


class PrivacyForms(forms.ModelForm):
    class Meta:
        model = Privacy
        fields = [
            'title',
            'discription',
        ]