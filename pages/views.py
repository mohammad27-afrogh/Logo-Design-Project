from django.shortcuts import render

from .models import AboutUs, Privacy
from portfolio.models import PortfolioItem
from orders.forms import LogoOrderForms


def home_page_view(request):

    portfolio = PortfolioItem.objects.filter(is_featured=True).prefetch_related('images').all()

    if request.method == 'POST':
        order_form = LogoOrderForms(request.POST)
        if order_form.is_valid():
            new_order = order_form.save(commit=False)
            new_order.user = request.user
            new_order.save()
            order_form = LogoOrderForms()
    else:
        order_form = LogoOrderForms()

    context = {
        'portfolio': portfolio,
        'order_form': order_form,
    }
    return render(request, 'home.html', context)


def about_us_view_page(request):
    about_us = AboutUs.objects.all()

    return render(request, 'pages/aboutus.html', context={'about_us': about_us})


def privacy_page_view(request):
    privacy = Privacy.objects.all()

    return render(request, 'pages/privacy.html', context={'privacy': privacy})
