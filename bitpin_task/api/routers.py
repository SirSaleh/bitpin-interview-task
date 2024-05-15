from rest_framework_nested import routers
from .views import ProductViewSet

router = routers.DefaultRouter()

router.register(r'products', ProductViewSet, basename='product')