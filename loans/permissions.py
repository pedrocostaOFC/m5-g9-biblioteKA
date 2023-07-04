from rest_framework import permissions
from books.models import Book


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(request.book_id)
        return obj == request.user or request.user.is_superuser

class IsDebitoAndAvailable(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True       
        if request.user.is_debt == True:
            return False
        if request.data["book_id"]:
            book_data = request.data["book_id"]
            book = Book.objects.get(id=book_data)     
            return book.is_available
             

class IsAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser