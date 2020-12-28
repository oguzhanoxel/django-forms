from django.contrib import admin
from .models import Book, Category


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'author', 'category', 'pages',
    )
    list_display_links = (
        'title', 'author', 'pages',
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title',
    )
    list_display_links = (
        'id', 'title',
    )


admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
