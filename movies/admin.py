from django.contrib import admin
from .models import Genre, Movie
# from django.contrib.admin.decorators import register


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    #  exlude = ('date_created', )
    list_display = ('title', 'number_in_stock', 'daily_rate')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
