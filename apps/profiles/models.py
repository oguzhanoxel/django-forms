from django.db import models

from apps.users.models import User
from apps.books.models import Book

class List(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
    )
    is_wished = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)
    is_reading = models.BooleanField(default=False)
    last_page = models.PositiveIntegerField(default=1)
    added_date = models.DateTimeField(auto_now_add=True)
    changed_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book.title
