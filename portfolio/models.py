from django.db import models
from django.urls import reverse

class PortfolioItem(models.Model):
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
        

    title = models.CharField(max_length=200, verbose_name="Project Name")
    slug = models.SlugField(unique=True, blank=True, null=False, allow_unicode=True)
    
    # شباهت با سفارش‌ها (برای فیلترینگ)
    style = models.CharField(max_length=50, choices=STYLE_CHOICES, verbose_name="style")
    personality = models.CharField(max_length=50, choices=PERSONALITY_CHOICES, verbose_name="personality")
    
    # جزئیات مربوط به نمونه کار
    description = models.TextField(verbose_name="project description", blank=True)
    is_featured = models.BooleanField(default=False, verbose_name="Display on the home page")
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title

    class Meta:
        verbose_name = "portfolio"
        verbose_name_plural = "portfolio"

    def get_absolute_url(self):
        return reverse('portfolio_detail_view', args=[self.slug])

class PortfolioImage(models.Model):
    project = models.ForeignKey(PortfolioItem, on_delete=models.CASCADE, related_name='images', verbose_name='PortfolioItem')
    image = models.ImageField(upload_to='portfolio/', blank=True, null=True)

    def __str__(self):
        return f'Image for {self.project.title}'
