from .routers import router, product_router

urlpatterns = [
]

urlpatterns += router.urls
urlpatterns += product_router.urls