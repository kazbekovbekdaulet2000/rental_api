from rest_framework import permissions
from django.contrib.auth.models import Group


class IsOwnerAndLandlord(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return Group.objects.get(name='landlord') in request.user.groups.all()

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user and Group.objects.get(name='landlord') in request.user.groups.all()


class ProductOwnerAndLandlord(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return Group.objects.get(name='landlord') in request.user.groups.all()

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.product.owner == request.user and Group.objects.get(name='landlord') in request.user.groups.all()


class ObjectOwnerOrAdmin(permissions.BasePermission):
    edit_methods = ("POST", "PUT", "PATCH", "DELETE")

    def has_permission(self, request, view):
        if permissions.IsAuthenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.owner.id == request.user.id or request.user.is_superuser:
            return True
        return False
