from django.urls import path, re_path

from .import views

app_name='blog'

urlpatterns = [
    path('', views.blog_page_view, name='blogs'),
    path('search/', views.blog_search, name='blog_search'),
    re_path(r'^(?P<blog_slug>[^/]+)/$', views.blog_detail_view, name='blog_detail_by_slug'),
]