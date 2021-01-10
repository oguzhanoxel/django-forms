from django.contrib import admin

from .models import List

class ListAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book', 'added_date', 'is_wished', 'is_reading', 'is_finished', 'last_page')
    list_display_links = ('user', 'book')

admin.site.register(List, ListAdmin)
