from django.contrib import admin
from .models import Book, Category, Comment


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

class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'book',
    )
    list_display_links = (
        'user', 'book',
    )


admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
