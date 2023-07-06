from rest_framework import permissions


class IsStudentOrCollaborator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.user.is_superuser:
            return True
        if request.user == obj:
            return True