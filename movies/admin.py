from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class MoviesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ('title',)}
    fields = ('title', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'is_published')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")
    get_html_photo.short_description = "Миниатюра"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_cat')
    list_display_links = ('id', 'title_cat')
    search_fields = ('id', 'title_cat')
    prepopulated_fields = {"slug": ("title_cat",)}


admin.site.register(Movies, MoviesAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title='Админ-панель сайта о женщинах'
admin.site.site_header='Админ-панель сайта о женщинах'


