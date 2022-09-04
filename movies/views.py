from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *


menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'},
]


def index(request):
    posts = Movies.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
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

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id={post_id}")





def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')



