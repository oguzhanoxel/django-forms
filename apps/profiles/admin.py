from django.contrib import admin

from .models import Wishlist

class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'added_date')
    list_display_links = ('user', 'book')

admin.site.register(Wishlist, WishlistAdmin)