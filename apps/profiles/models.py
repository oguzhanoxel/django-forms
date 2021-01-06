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
    changed_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book.title

class FinishedList(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
    )
    is_finished = models.BooleanField(default=False)
    added_date = models.DateTimeField(auto_now_add=True)
    changed_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book.title

class ReadingList(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
    )
    last_page = models.PositiveIntegerField(default=1, null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)
    changed_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book.title

    def update_last_page(self, page_num):
        self.last_page = page_num
