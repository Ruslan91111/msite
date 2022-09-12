from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, FormView
from .utils import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class MoviesHome(DataMixin, ListView):
    model = Movies
    template_name = 'movies/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Movies.objects.filter(is_published=True).select_related('cat')


def about(request):
    contact_list = Movies.objects.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'movies/about.html', {'page_obj': page_obj, 'menu': menu,'title': 'О сайте'})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'movies/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
       context = super().get_context_data(**kwargs)
       c_def = self.get_user_context(title="Добавление статьи")
       return dict(list(context.items()) + list(c_def.items()))

class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'movies/contact.html'
    success_url = reverse_lazy('home')



class ShowPost(DataMixin, DetailView):
    model = Movies
    template_name = 'movies/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class MoviesCategory(DataMixin, ListView):
    model = Movies
    template_name = 'movies/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Movies.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Категория - ' + str(c.title_cat),
                                       cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'movies/register.html'
    success_url = reverse_lazy('login')

    def ge_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'movies/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')


