from django.contrib import admin
from .models import *


class MoviesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_cat')
    list_display_links = ('id', 'title_cat')
    search_fields = ('id', 'title_cat')


class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')


admin.site.register(Movies, MoviesAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Actor, ActorAdmin)




