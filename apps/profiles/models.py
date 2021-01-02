from django.db import models

from apps.users.models import User
from apps.books.models import Book

class Wishlist(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
    )
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book.title
