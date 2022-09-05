from django.contrib import admin
from .models import *


class MoviesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_cat')
    list_display_links = ('id', 'title_cat')
    search_fields = ('id', 'title_cat')
    prepopulated_fields = {"slug": ("title_cat",)}


admin.site.register(Movies, MoviesAdmin)
admin.site.register(Category, CategoryAdmin)




