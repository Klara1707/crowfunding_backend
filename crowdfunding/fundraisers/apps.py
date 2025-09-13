from django.apps import AppConfig
from rest_framework import permissions

class FundraisersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fundraisers'

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only for the owner
        return obj.owner == request.user
