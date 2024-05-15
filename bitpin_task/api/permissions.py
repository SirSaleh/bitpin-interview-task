from rest_framework.permissions import BasePermission


class ProductPermission():

    def has_permission(self, request, view):
        if request.method == "GET":
            # everyone can see details of the
            # products
            return True
        else:
            # Only superusers can Create, 
            # Update and delete the Products
            if request.user.is_superuser:
                return True
            return False
