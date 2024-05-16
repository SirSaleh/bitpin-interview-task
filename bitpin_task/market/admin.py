from django.contrib import admin
from .models import Product, ProductRating

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class ProductRatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'rating']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductRating, ProductRatingAdmin)
