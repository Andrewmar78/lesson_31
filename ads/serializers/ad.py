from rest_framework.generics import get_object_or_404
from rest_framework import serializers

from ads.models.ad import Ad
from ads.models.category import Category
from users.models import User


class AdSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(required=False, queryset=User.objects.all(), slug_field='username')
    category = serializers.SlugRelatedField(required=False, queryset=Category.objects.all(), slug_field='name')

    class Meta:
        model = Ad
        fields = '__all__'


class AdCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    author = serializers.SlugRelatedField(required=False, queryset=User.objects.all(), slug_field='username')
    category = serializers.SlugRelatedField(required=False, queryset=Category.objects.all(), slug_field='name')
    image = serializers.ImageField(required=False)

    class Meta:
        model = Ad
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._author = self.initial_data.pop('author')
        self._category = self.initial_data.pop('category')
        # self._author_id = self.initial_data.pop('author_id')
        # self._category_id = self.initial_data.pop('category_id')
        return super().is_valid(raise_exception=raise_exception)

    # def create(self, validated_data):
    #     ad = Ad.objects.create(**validated_data)
    #     for author in self._author:
    #         author_obj, _ = author.objects.get_or_create(name=author)
    #         ad.author.add(author_obj)
    #
    #     for category in self._category:
    #         category_obj, _ = category.objects.get_or_create(name=category)
    #         ad.category.add(category_obj)

    def create(self, validated_data):
        ad = Ad.objects.create(name=validated_data.get('name'), price=validated_data.get('price'),
                               description=validated_data.get('description'),
                               is_published=validated_data.get('is_published'))
        ad.author = get_object_or_404(User, pk=self._author)
        ad.category = get_object_or_404(Category, pk=self._category)
        # ad.author = get_object_or_404(User, pk=self._author_id)
        # ad.category = get_object_or_404(Category, pk=self._category_id)

        ad.save()
        return ad


class AdUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    image = serializers.ImageField(required=False)
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    category = serializers.SlugRelatedField(required=False, queryset=Category.objects.all(), slug_field='name')

    class Meta:
        model = Ad
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._category = self.initial_data.pop('category')
        # self._category_id = self.initial_data.pop('category_id')
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        ad = super().save()
        ad.category = get_object_or_404(Category, pk=self._category)
        # ad.category = get_object_or_404(Category, pk=self._category_id)
        ad.save()

        return ad


class AdImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    category = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    price = serializers.IntegerField(read_only=True)
    is_published = serializers.BooleanField(read_only=True)

    class Meta:
        model = Ad
        fields = '__all__'
