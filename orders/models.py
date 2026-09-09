from django.db import models
from django.conf import settings

class ReferenceImage(models.Model):
    # این مدل را حتما باید داشته باشی تا ManyToMany کار کند
    image = models.ImageField(upload_to='references/')
    url = models.URLField(blank=True, null=True, help_text='Link to Pinterest or other sources')

    def str(self):
        return f"Reference {self.id}"

class LogoOrder(models.Model):
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
    
    STATUS_CHOICES = [
        ('pending', 'Pending review'),
        ('confirmed', 'Confirmed & Approved'),
        ('designing', 'In Progress (Designing)'),
        ('revision', 'Under Revision'),
        ('completed', 'Completed & Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    # --- User & Basic Info ---
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name='logo_orders')
    name = models.CharField(max_length=120, null=True, blank=True, help_text='The brand name to be included in the design')

    # --- Design Details ---
    style = models.CharField(max_length=20, choices=STYLE_CHOICES, null=True, blank=True, help_text='The visual style of the logo.')
    personality = models.CharField(max_length=20, choices=PERSONALITY_CHOICES, null=True, blank=True, help_text='The brand personality (e.g., formal, playful, or luxury).')
    color_preferences = models.CharField(max_length=200, null=True, blank=True, help_text='Preferred colors (e.g., black and gold).')
    usage = models.CharField(max_length=200, blank=True, help_text='Target usage (e.g., website, business card, etc.).')

    # --- Project Scope ---
    brief_text = models.TextField(null=True, blank=True, help_text='Detailed description of the brand and requirements.') 
    budget = models.DecimalField(max_digits=12, decimal_places=0, help_text='Budget in Toman (e.g., 5000000).')
    deadline = models.DateField(null=True, blank=True, help_text='Expected delivery date.')

    # --- Assets ---
    references = models.ManyToManyField(ReferenceImage, blank=True, help_text='Upload reference images or provide links.')

    # --- Admin & Management ---
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    admin_notes = models.TextField(blank=True, help_text='Internal notes for admin use only.')
    final_file = models.FileField(upload_to='deliveries/', null=True, blank=True, help_text='The final high-resolution design files.')

    # --- Metadata ---
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def str(self):
        return f"Order {self.id} - {self.name}"
