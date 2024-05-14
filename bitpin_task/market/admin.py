from django.contrib import admin
from .models import Product, ProductRating

class ProductAdmin(admin.ModelAdmin):
    pass


class ProductRatingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductRating, ProductRatingAdmin)
