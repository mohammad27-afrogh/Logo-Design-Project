from django.urls import path, re_path

from . import views

app_name='page'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('aboutus/', views.about_us_view_page, name='aboutus'),
    path('privacy/', views.privacy_page_view, name='privacy'),
]
