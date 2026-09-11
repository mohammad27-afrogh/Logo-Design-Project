from django.urls import path, re_path

from . import views

app_name = 'portfolio'

urlpatterns = [
    re_path(r'(?P<portfolio_slug>[^/]+)/$', views.portfolio_detail_view, name='portfolio_detail_view'),
]
