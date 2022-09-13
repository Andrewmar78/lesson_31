from datetime import date, timedelta
from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.exceptions import ValidationError
from django.core.validators import EmailValidator

from ads.models.location import Location
from authentication.constants import min_age, not_allowed_domains


def check_min_age(birth_date: date):
    if (date.today() - birth_date) < timedelta(days=min_age * 365):
        raise ValidationError(
            f"{birth_date} - person is too young."
        )


def check_email(email):
    domain = email.split('@')[1]
    if domain in not_allowed_domains:
        raise ValidationError(
            f"{domain} is not allowed."
        )

    # validator = EmailValidator(message="Enter a valid email address", allowlist=[allowed_domains])


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
    birth_date = models.DateField(null=True, validators=[check_min_age])
    email = models.EmailField(null=True, unique=True, validators=[check_email])

    def __str__(self):
        return self.username
