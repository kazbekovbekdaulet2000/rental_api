from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user

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