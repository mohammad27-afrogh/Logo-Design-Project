from django.urls import path, re_path

from . import views

app_name='order'

urlpatterns = [
    path('create/', views.order_create_view, name='order_create'),
    path('my_orders', views.my_orders_view, name='my_orders'),
    re_path(r'(?P<order_name>[^/]+)/$', views.my_order_details_view, name='my_order_details_by_name'),
]
