from django.contrib.auth.models import AnonymousUser
from rest_framework import permissions
from rest_framework.permissions import BasePermission

from authentication.models import User
from users.views import user


class AdCreatePermission(BasePermission):
    message = 'Only authorized user can create the ad'

    def has_permission(self, request, view):
        if not isinstance(request.user, AnonymousUser):
            return True
        return False


class AdUpdateDeletePermission(BasePermission):
    message = 'Only owner user, amdin and moderators can update or delete the ad'

    def has_permission(self, request, view):
        if isinstance(request.user, AnonymousUser):
            return False
        if request.user.role == User.ADMIN or request.user.role == User.MODERATOR:
            return True
        return False
