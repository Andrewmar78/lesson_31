import factory.django
from pytest_factoryboy import register
from ads.models.ad import Ad
from ads.models.category import Category
from authentication.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('name')
    password = 'user_password'


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('name')


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = "Test ad more than 10 letters"
    price = 1000
    is_published = False
    author = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)


register(AdFactory)
register(CategoryFactory)
register(UserFactory)
