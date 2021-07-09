from django.db import models


class Book(models.Model):
    book_id = models.CharField(
        max_length=20
    )
    title = models.CharField(
        max_length=120,
        blank=True,
        null=True
    )
    authors = models.CharField(
        max_length=120,
        blank=True,
        null=True
    )
    published_date = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )
    categories = models.CharField(
        max_length=120,
        blank=True,
        null=True
    )
    average_rating = models.IntegerField(
        blank=True,
        null=True
    )
    ratings_count = models.IntegerField(
        blank=True,
        null=True
    )
    thumbnail = models.URLField(
        blank=True,
        null=True
    )
