from django.contrib.auth.models import User
from django.db.models import Avg
from django.db.models.functions import TruncHour
from market.models import ProductRating
from rest_framework import serializers
from market.models import Product, ProductRating


class ProductSerializer(serializers.ModelSerializer):
    overal_rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', "overal_rating"]
    
    def get_overal_rating(self, obj):
        hourly_rating = ProductRating.objects.annotate(hour=TruncHour('timestamp'))
        hourly_average_ratings = hourly_rating.values('hour').annotate(hourly_avg=Avg('rating'))
        overal_rating = hourly_average_ratings.aggregate(overall_avg=Avg('hourly_avg'))

        return round(overal_rating['overall_avg'], 2)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']


class ProductRatingSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = ProductRating
        fields = ['id', 'user', 'rating']