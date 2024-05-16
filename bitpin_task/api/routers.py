from rest_framework_nested import routers
from .views import ProductViewSet, ProductRatingViewSet

router = routers.DefaultRouter()

router.register(r'products', ProductViewSet, basename='product')

product_router = routers.NestedDefaultRouter(router, r'products', lookup='product')
product_router.register(r'ratings', ProductRatingViewSet, basename="products_rating")