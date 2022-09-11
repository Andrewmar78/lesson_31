from django.contrib.auth.models import AbstractUser
from django.db import models
from ads.models.location import Location


class User(AbstractUser):
    ADMIN = "admin"
    MODERATOR = "moderator"
    MEMBER = "member"
    ROLES = [(ADMIN, 'Администратор'), (MEMBER, 'Пользователь'), (MODERATOR, 'Модератор')]

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=9, null=True, choices=ROLES, default=MEMBER)
    age = models.PositiveSmallIntegerField()
    locations = models.ManyToManyField(Location, related_name="user")
    # location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username
