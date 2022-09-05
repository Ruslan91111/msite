from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *


def index(request):
    posts = Movies.objects.all()

    context = {
        'posts': posts,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'movies/index.html', context=context)


def about(request):
    return render(request, 'movies/about.html', {'menu': menu, 'title': "ABOUT"})


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse("Войти")


def show_post(request, post_slug):
    post = get_object_or_404(Movies, slug=post_slug)

    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'movies/post.html', context=context)


def show_category(request, cat_slug):
    posts = Movies.objects.filter(cat__slug=cat_slug)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'title': 'Главная страница',
        'cat_selected': cat_slug,

    }
    return render(request, 'movies/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')



