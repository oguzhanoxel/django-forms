from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'author', 'pages',
    )
    list_display_links = (
        'title', 'author', 'pages',
    )


admin.site.register(Book, BookAdmin)
