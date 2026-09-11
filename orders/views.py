from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import LogoOrder

@login_required
def my_orders_view(request):
    # 1. دسترسی به شیء کاربر احراز هویت شده
    current_user = request.user
    
    my_orders = LogoOrder.objects.filter(user=current_user).prefetch_related('items').all()

    context = {
        'my_orders': my_orders,
    }

    return render(request, 'orders/my_orders.html', context)