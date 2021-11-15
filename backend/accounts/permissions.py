from rest_framework import permissions


class UpdateOwnUser(permissions.BasePermission):
    """Allow user to just change their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check if user is trying to change their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
