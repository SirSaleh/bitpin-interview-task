from django.urls import path
from .views import HomePage, ProductDetail

urlpatterns = [
    path(r'', HomePage.as_view(), name="home"),
    path(r'products/<int:pk>', ProductDetail.as_view(), name="product_detail"),
]
