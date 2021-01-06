from django.contrib import admin

from .models import Wishlist, FinishedList, ReadingList

class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'added_date')
    list_display_links = ('user', 'book')

class FinishedListAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'is_finished', 'added_date')
    list_display_links = ('user', 'book')

class ReadingListAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'last_page', 'added_date')
    list_display_links = ('user', 'book')

admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(FinishedList, FinishedListAdmin)
admin.site.register(ReadingList, ReadingListAdmin)