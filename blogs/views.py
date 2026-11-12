from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.db.models import Prefetch

from .models import Blog, CommentBlog
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

    approved_replies_prefetch = Prefetch(
        'replies',
        queryset = CommentBlog.objects.filter(is_approved=True),
        to_attr = 'approved_replies'
    )

    blog_detail = get_object_or_404(Blog, slug=blog_slug)
    blog_detail.view_count += 1
    blog_detail.save()

    try:
        previous_blog = blog_detail.get_previous_by_date_time_create()
    except Blog.DoesNotExist:
        previous_blog = None

    try:
        next_blog = blog_detail.get_next_by_date_time_create()
    except Blog.DoesNotExist:
        next_blog = None

    blog_comments = blog_detail.comments.filter(is_approved=True, parent__isnull=True).prefetch_related(approved_replies_prefetch)
    total_comment = blog_detail.comments.filter(is_approved=True).count()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.blog = blog_detail
            new_comment.user = request.user if request.user.is_authenticated else None

            new_comment.is_approved = False
            new_comment.save()

            messages.success(request, 'Your comment has been successfully submitted and will be displayed after approval.')
            return redirect('blog:blog_detail_by_slug', blog_slug=blog_detail.slug)

    else:
        comment_form = CommentForm()

    context = {
        'blog': blog_detail,
        'comments': blog_comments,
        'total_comment': total_comment,
        'comment_form': comment_form,
        'previous_blog': previous_blog,
        'next_blog': next_blog,
    }

    return render(request, 'blogs/blog_detail.html', context)
