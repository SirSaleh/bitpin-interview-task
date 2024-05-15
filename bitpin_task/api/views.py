from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.response import Response

from .serializers import ProductSerializer
from .permissions import ProductPermission
from .paginations import ProductPagination

from market.models import Product


class ProductViewSet(viewsets.ModelViewSet, mixins.UpdateModelMixin):#, mixins.RetrieveModelMixin, mixins.ListModelMixin,
                     #mixins.CreateModelMixin, mixins.UpdateModelMixin,
                     #mixins.DestroyModelMixin):
    serializer_class = ProductSerializer
    permission_classes = (ProductPermission, )
    pagination_class = ProductPagination

    def get_queryset(self):
        return Product.objects.all().order_by('-id')
    
    def get_object(self):
        qs = Product.objects.all()
        obj = get_object_or_404(qs, id=self.kwargs['pk'])
        return obj