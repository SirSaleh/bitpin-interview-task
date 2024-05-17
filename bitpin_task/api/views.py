from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import ProductSerializer, ProductRatingSerializer
from .permissions import ProductPermission, ProductRatingPermission
from .paginations import ProductPagination, ProductRatingPagination

from market.models import Product, ProductRating


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = (ProductPermission, )
    pagination_class = ProductPagination

    def get_queryset(self):
        return Product.objects.all().order_by('-id')
    
    def get_object(self):
        qs = Product.objects.all()
        obj = get_object_or_404(qs, id=self.kwargs['pk'])
        return obj


class ProductRatingViewSet(viewsets.ModelViewSet):
    serializer_class = ProductRatingSerializer
    permission_classes = (ProductRatingPermission, )
    pagination_class = ProductRatingPagination

    def get_queryset(self):
        return ProductRating.objects.filter(product__id=self.kwargs['product_pk']).order_by('-id')

    def get_object(self):
        qs = ProductRating.objects.all()
        obj = get_object_or_404(qs, id=self.kwargs['pk'])
        return obj
    
    def create(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            raise
        current_rating_qs = ProductRating.objects.filter(user__pk=self.request.user.id,
                                                         product__pk=self.kwargs['product_pk'])
        
        if current_rating_qs:
            # There exist a rating from this user
            # for this product, so it should be upgraded
            product_rating = current_rating_qs.get()
            product_rating.rating = self.request.data.get('rating')
            product_rating.save()
        else:
            product = Product.objects.get(id=self.kwargs['product_pk'])
            product_rating = ProductRating.objects.create(user=self.request.user, product=product,
                                         rating =int(self.request.data.get('rating')))
        
        return Response(self.serializer_class(product_rating, many=False).data, status=201)

