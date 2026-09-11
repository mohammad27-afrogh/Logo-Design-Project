from django.contrib import admin

from .models import PortfolioItem, PortfolioImage

class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra = 3


@admin.register(PortfolioItem)
class PortfolioItemInline(admin.ModelAdmin):
    list_display = [
        'title',
    ]
    inlines = [PortfolioImageInline]
