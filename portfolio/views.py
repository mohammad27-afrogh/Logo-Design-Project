from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import PortfolioItem

def portfolio_page_view(request):
        
    NUMBER_PAGINATOR = 10
    paginator = Paginator(PortfolioItem, NUMBER_PAGINATOR)
    page_number = request.GET.get('page', 1)

    try:
        portfo_obj = paginator.page(page_number)
    except PageNotAnInteger:
        portfo_obj = paginator.page(1)
    except EmptyPage:
        portfo_obj = paginator.page(paginator.num_pages)

    context={
        'portfolios': portfo_obj.object_list,
        'portfo_obj': portfo_obj,
        'paginator': paginator,
        'is_paginated': portfo_obj.has_other_pages(),
    }

    return render(request, 'portfolio/list_portfolio.html', context)


def portfolio_detail_view(request, portfolio_slug):
    portfolio = get_object_or_404(PortfolioItem, slug=portfolio_slug)

    context = {
        'portfolio': portfolio,
    }

    return render(request, 'portfolio/detail_portfolio.html', context)
