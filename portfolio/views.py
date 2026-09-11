from django.shortcuts import render, get_object_or_404

from .models import PortfolioItem

def portfolio_detail_view(request, portfolio_slug):
    portfolio = get_object_or_404(PortfolioItem, slug=portfolio_slug)

    context = {
        'portfolio': portfolio,
    }

    return render(request, 'portfolio/detail_portfolio.html', context)
