from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("MAIN PAGE")

def categories(request):
    return HttpResponse("<h1>Статьи по категориям</h1>")
