from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *


menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def index(request):
    posts = Movies.objects.all()
    return render(request, 'movies/index.html', {'posts': posts, 'menu': menu, 'title': "Главная страница"})


def about(request):
    return render(request, 'movies/about.html', {'menu': menu, 'title': "ABOUT"})


def categories(request, category):
    if request.POST:
        print(request.POST)

    return HttpResponse(f"<h1>Статьи по категории</h1><p>{category}</p>")


def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=True)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')



