from django.shortcuts import render, redirect, reverse
from .models import *
from django.core.paginator import Paginator
from .forms import CommentForm


# from .forms import SearchForm, CommentForm


def homeView(request):
    article_list = Article.objects.order_by('-publish_date').filter(published=True,
                                                                    program__program_name__iexact='Bigg Boss S14')
    paginator = Paginator(article_list, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # form = SearchForm(request.POST or None)
    # if request.method == 'POST':
    #     page_obj = Article.objects.filter(program=True, publish_date__exact=True)

    context = {
        'article_list': page_obj,
        # 'form': form,
    }
    return render(request, 'mainapp/home.html', context)


def detailView(request, slug):
    article = Article.objects.get(slug=slug)
    side_article = Article.objects.filter(published=True, program__program_name__iexact='Bigg Boss S14').order_by(
        '-publish_date')[0:3]

    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        comment = form.save(commit=False)
        if form.is_valid():
            comment.article = article
            comment.save()
            return redirect('main_app:home')
    else:
        form = CommentForm()

    context = {
        'article': article,
        'form': form,
        'side_article': side_article,
    }
    return render(request, 'mainapp/detail.html', context)


def videoView(request, slug):
    article = Article.objects.get(slug=slug)
    side_article = Article.objects.filter(published=True,
                                          program__program_name__iexact='Bigg Boss S14').order_by(
        '-publish_date')[0:3]
    context = {
        'article': article,
        'side_article': side_article,
    }
    return render(request, 'mainapp/video.html', context)


def partVideoView(request, slug):
    article = Article.objects.get(slug=slug)
    side_article = Article.objects.filter(published=True,
                                          program__program_name__iexact='Bigg Boss S14').order_by(
        '-publish_date')[0:3]
    context = {
        'article': article,
        'side_article': side_article,
    }
    return render(request, 'mainapp/part_video.html', context)


def moviehomeView(request):
    article_list = Article.objects.order_by('-publish_date').filter(published=True,
                                                                    program__program_name__iexact='Movies')
    paginator = Paginator(article_list, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # form = SearchForm(request.POST or None)
    # if request.method == 'POST':
    #     page_obj = Article.objects.filter(program=True, publish_date__exact=True)

    context = {
        'article_list': page_obj,
        # 'form': form,
    }
    return render(request, 'mainapp/movies.html', context)