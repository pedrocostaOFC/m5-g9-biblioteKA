from rest_framework import permissions
from copies.models import Copy


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(request.book_id)
        return obj == request.user or request.user.is_superuser

class IsDebitoAndAvailable(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True       
        if request.user.is_blocked == True:
            return False
        if request.data["copy_id"]:
            copy_data = request.data["copy_id"]
            copy = Copy.objects.get(id=copy_data)     
            return copy.is_avaiable
             

class IsAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser