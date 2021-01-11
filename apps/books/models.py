from django.db import models
from django.utils import timezone
from apps.users.models import User

class Category(models.Model):
    title = models.CharField(
        max_length=255,
    )

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

class Book(models.Model):
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    image = models.ImageField(
        upload_to='Books/', null=True, blank=True,
    )
    title = models.CharField(
        max_length=255, null=True, blank=True,
    )
    author = models.CharField(
        max_length=255, null=True, blank=True,
    )
    desc = models.TextField(
        null=True, blank=True,
    )
    pages = models.PositiveIntegerField(
        null=True, blank=True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

class Comment(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text