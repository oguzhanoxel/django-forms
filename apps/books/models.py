from django.db import models

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

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
