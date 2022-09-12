from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    # Added
    slug = models.CharField(min_length=5, max_length=10, unique=True)


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
