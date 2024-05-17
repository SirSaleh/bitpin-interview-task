from django.urls import path
from .views import HomePage, ProductDetail, CreateProduct

urlpatterns = [
    path(r'', HomePage.as_view(), name="home"),
    path(r'products/<int:pk>', ProductDetail.as_view(), name="product_detail"),
    path(r'products/create', CreateProduct.as_view(), name="create_product")
]
