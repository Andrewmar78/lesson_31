from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from authentication.models import User
from users.serializers import UserListSerializer, UserCreateSerializer, UserUpdateSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]

# class UserCreateView(CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserCreateSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
