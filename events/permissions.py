from rest_framework.permissions import BasePermission, SAFE_METHODS


class SafeMethodPermission(BasePermission):
    def has_permission(self, request, view):
        # SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']
        if request.method not in SAFE_METHODS:
            return request.user.is_staff or request.user.is_superuser
        return True