from django.urls import path, re_path

from . import views

app_name='order'

urlpatterns = [
    path('my_orders', views.my_orders_view, name='my_orders'),
]
