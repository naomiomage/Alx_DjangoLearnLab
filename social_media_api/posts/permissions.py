from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit or delete it.
    Read-only access is allowed to everyone.
    """

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS: GET, HEAD, OPTIONS are allowed
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only for the author
        return hasattr(obj, 'author') and obj.author == request.user
