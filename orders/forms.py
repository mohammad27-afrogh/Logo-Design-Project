from django import forms
from .models import LogoOrder, ReferenceImage
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field

class AddressFormOrder(forms.Form):
    
    STYLE_CHOICES = [
        ('minimal', 'Minimal and simple'),
        ('typography', 'Typography (text-based)'),
        ('mascot', 'Mascots (Character-based)'),
        ('vintage', 'Classic and vintage'),
        ('modern', 'Modern and geometric'),
        ('abstract', 'Abstract'),
    ]

    PERSONALITY_CHOICES = [
        ('formal', 'Formal and serious'),
        ('playful', 'Happy and playful'),
        ('luxury', 'Luxurious and Exclusive'),
        ('affordable', 'Economic and General'),
        ('bold', 'Bold and powerful'),
        ('elegant', 'Elegant and dignified'),
    ]

    CURRENCY_CHOICES = [
        ('IRT', 'Toman (تومان)'),
        ('USD', 'US Dollar ($)'),
    ]

    name = forms.CharField(required=True, max_length=120, help_text='The brand name to be included in the design')
    style = forms.ChoiceField(required=True, choices=[('', "The visual style of the logo...")] + STYLE_CHOICES)
    personality = forms.ChoiceField(required=True, choices=[('', "The brand personality...")] + PERSONALITY_CHOICES)
    color_preferences = forms.CharField(required=True, max_length=200, help_text='Preferred colors (e.g., black and gold).')
    usage = forms.CharField(required=True, max_length=200, help_text='Target usage (e.g., website, business card, etc.).')
    
    brief_text = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 4}), help_text='Detailed description.') 
    
    # واحد پول و بودجه
    currency = forms.ChoiceField(required=True, choices=CURRENCY_CHOICES, initial='USD')
    budget = forms.DecimalField(required=True, max_digits=12, decimal_places=0, help_text='Your estimated budget.')

    deadline = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}), help_text='Expected delivery date.')

    reference_image_file = forms.ImageField(required=False, help_text='Upload a reference image or sketch.')
    reference_url_link = forms.URLField(required=False, help_text='Provide a URL link (e.g., Pinterest).')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'order-form needs-validation'
        self.helper.attrs = {'enctype': 'multipart/form-data'}
        
        # چیدمان حرفه‌ای فیلدها با Crispy Layout
        self.helper.layout = Layout(
            'name',
            'style',
            'personality',
            'color_preferences',
            'usage',
            'brief_text',
            # قرار دادن بودجه و واحد پول کنار هم در یک سطر
            Row(
                Column('budget', css_class='form-group col-md-8 mb-3'),
                Column('currency', css_class='form-group col-md-4 mb-3'),
                css_class='form-row'
            ),
            'deadline',
            'reference_image_file',
            'reference_url_link',
        )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        ref_image = cleaned_data.pop('reference_image_file', None)
        ref_url = cleaned_data.pop('reference_url_link', None)

        order = LogoOrder.objects.create(**cleaned_data)

        if ref_image or ref_url:
            new_ref = ReferenceImage.objects.create(
                image=ref_image if ref_image else None,
                url=ref_url if ref_url else ''
            )
            order.references.add(new_ref)

        if commit:
            order.save()

        return order


class ReferenceImageForms(forms.ModelForm):
    class Meta:
        model = ReferenceImage
        fields = [
            'image',
            'url',
        ]
