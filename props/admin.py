from django.contrib import admin
from .models import Taste, Prop
#  from django.contrib.admin.decorators import register


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class PropAdmin(admin.ModelAdmin):
    #  exlude = ('date_created', )
    list_display = ('title', 'number_in_stock', 'daily_rate')


admin.site.register(Taste, GenreAdmin)
admin.site.register(Prop, PropAdmin)
