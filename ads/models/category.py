from django.core.validators import MinLengthValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(
        max_length=10,
        null=True,
        unique=True,
        validators=[MinLengthValidator(5, 'the field must contain at least 5 characters')],
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
