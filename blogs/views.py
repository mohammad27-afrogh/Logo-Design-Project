from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Blog
from .forms import CommentForm
from django.db.models import Q
from datetime import timedelta
from django.utils import timezone


def blog_page_view(request):
    blog = Blog.objects.all()
    
    NUMBER_PAGINATOR = 5
    paginator = Paginator(blog, NUMBER_PAGINATOR)
    page_number = request.GET.get('page', 1)

    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    default_time = timezone.now()
    one_month_ago = default_time - timedelta(days=60)

    latest_blog = blog.filter(Q(date_time_create__gte=one_month_ago) & Q(date_time_create__lte=default_time))


    context = {
        'blogs': page_obj.object_list,
        'page_obj': page_obj,
        'paginator': paginator,
        'is_paginated': page_obj.has_other_pages(),
        'latest_blog': latest_blog,
    }

    return render(request, 'blogs/blog.html', context)


def blog_search(request):
    # کلمه ای که کاربر سرچ کرده را میگیریم (اگر خالی بود رشته خالی برمیگرداند)
    query = request.GET.get('q', '')
    results = []

    if query:
        # جستجو در عنوان یا متن مقالات
        results = Blog.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        ).distinct()

    context = {
        'query': query,
        'results': results,
    }

    return render(request, 'blogs/search_results.html', context)


def blog_detail_view(request, blog_slug):

    blog_detail = get_object_or_404(Blog, slug=blog_slug)
    blog_detail.view_count += 1
    blog_detail.save()

    blog_comments = blog_detail.comments.all()
    total_comment = len(blog_comments)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.blog = blog_detail
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    context = {
        'blog': blog_detail,
        'comments': blog_comments,
        'total_comment': total_comment,
        'comment_form': comment_form,
    }

    return render(request, 'blogs/blog_detail.html', context)
