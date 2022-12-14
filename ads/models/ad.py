from django.core.validators import MinLengthValidator
from django.db import models

from ads.models.category import Category
from authentication.models import User


class Ad(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(10, 'The field must contain at least 10 characters')]
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.PositiveSmallIntegerField(default=0)
    description = models.TextField(max_length=2000, null=True)
    is_published = models.BooleanField(default=None)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.name
