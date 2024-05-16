from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include(('market.urls', 'market'), namespace="market"), name="market"),
    path('api/', include(('api.urls', 'api'), namespace="api"), name="api"),
    path('admin/', admin.site.urls),
]
