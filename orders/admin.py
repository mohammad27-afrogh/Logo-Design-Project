from django.contrib import admin

from .models import ReferenceImage, LogoOrder

@admin.register(ReferenceImage)
class ReferenceImageAdmin(admin.ModelAdmin):
    list_display = [
        'url',
    ]


@admin.register(LogoOrder)
class LogoOrderAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'name',
        'usage',
        'budget',
        'status',
        'created_at',
        'updated_at',
    ]
