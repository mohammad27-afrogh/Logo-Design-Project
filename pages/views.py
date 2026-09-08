from django.shortcuts import render
from django.views.generic import TemplateView

from .models import AboutUs, Privacy
class HomePageView(TemplateView):
    template_name = 'home.html'

def about_us_view_page(request):
    about_us = AboutUs.objects.all()

    return render(request, 'pages/aboutus.html', context={'about_us': about_us})


def privacy_page_view(request):
    privacy = Privacy.objects.all()

    return render(request, 'pages/privacy.html', context={'privacy': privacy})
