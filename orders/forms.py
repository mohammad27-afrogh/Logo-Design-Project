from django import forms

from .models import ReferenceImage, LogoOrder

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

    # --- User & Basic Info ---
    name = forms.CharField(required=True, max_length=120, help_text='The brand name to be included in the design')

    # --- Design Details ---
    style = forms.ChoiceField(required=True, choices=[('', "The visual style of the logo...")] + STYLE_CHOICES)
    personality = forms.ChoiceField(required=True, choices=[('', "The brand personality (e.g., formal, playful, or luxury)...")] + PERSONALITY_CHOICES)
    color_preferences = forms.CharField(required=True, max_length=200, help_text='Preferred colors (e.g., black and gold).')
    usage = forms.CharField(required=True, max_length=200, help_text='Target usage (e.g., website, business card, etc.).')

    # --- Project Scope ---
    brief_text = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows':4, 'cols':40}), help_text='Detailed description of the brand and requirements.') 
    budget = forms.DecimalField(required=True, max_digits=12, decimal_places=0, help_text='Budget in Toman (e.g., 5000000).')
    deadline = forms.DateField(required=True, help_text='Expected delivery date.')

    # --- Assets ---
    references = forms.ModelMultipleChoiceField(queryset=ReferenceImage.objects.all(), required=True, widget=forms.CheckboxSelectMultiple, help_text='Upload reference images or provide links.')

    # اضافه کردن متد save اگر نیاز دارید داده ها را در مدل Order ذخیره کنید
    def save(self, commit=True):
        order_data = self.cleaned_data
        # استخراج مقادیر به جز references
        references = order_data.pop(
            'references'
            # جداکردن references از بقیه
        , None) 

        # ایجاد یا ذخیره شیء LogoOrder با بقیه اطلاعات
        order = LogoOrder.objects.create(
            **order_data
            # تمام فیلدها را یکجا روی مدل ست میکند
        )

        # مدیریت رابطه MenyToMeny بعد از ذخیره شدن اولیه شیء
        if references:
            order.references.set(references)

        return order


class ReferenceImageForms(forms.ModelForm):
    class Meta:
        model = ReferenceImage
        fields = [
            'image',
            'url',
        ]
