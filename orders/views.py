from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import LogoOrder
from .forms import AddressFormOrder

@login_required
def order_create_view(request):

    if request.method == 'POST':
        form = AddressFormOrder(request.POST)
        if form.is_valid():
            order_obj = form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()

    else:
        form = AddressFormOrder()

    context={
        'form': form,
    }
    
    return render (request, 'orders/place_order.html', context)


@login_required
def my_orders_view(request):
    
    my_orders = request.user.logo_orders.all().order_by('-created_at')

    context = {
        'my_orders': my_orders,
    }

    return render(request, 'orders/my_orders.html', context)


def my_order_details_view(request, order_name):
    order = get_object_or_404(LogoOrder, name=order_name)

    context = {
        'order': order,
    }

    return render(request, 'orders/my_order_details.html', context)
