from django.contrib.auth.models import User
from rest_framework import serializers
from market.models import Product, ProductRating


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'title']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']


class ProductRatingSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = ProductRating
        fields = ['id', 'user', 'rating']