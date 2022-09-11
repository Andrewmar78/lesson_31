from rest_framework import serializers

from authentication.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    # author = serializers.SlugRelatedField(required=False, queryset=User.objects.all(), slug_field='username')
    # category = serializers.SlugRelatedField(required=False, queryset=Category.objects.all(), slug_field='name')

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(user.password)
        user.save()
        return user
