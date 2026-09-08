from django.contrib import admin

from .models import AboutUs, Privacy

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = [
        'title',
    ]

@admin.register(Privacy)
class PrivacyAdmin(admin.ModelAdmin):
    list_display = [
        'title',
    ]
