from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        if request.user and request.user.is_staff:
            return True
        else:
            return request.method in SAFE_METHODS



