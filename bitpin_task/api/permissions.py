from rest_framework.permissions import BasePermission


class ProductPermission(BasePermission):

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


class ProductRatingPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in ["GET", "POST"]:
            # everyone can see details of the
            # ratings of the products and create
            # a new one
            return True
        elif request.method in ['DELETE']:
            # No one can delete a rating
            # (Based on the Bitpin task details)
            return False
        else:
            # Only Owners of the ratings 
            # would be able to modify it
            if request.user.username == obj.user.username:
                return True
            return False
