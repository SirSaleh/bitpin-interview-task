from django.urls import path
from .views import HomePage

urlpatterns = [
    path(r'', HomePage.as_view(), name="home"),
]
