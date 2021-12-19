from rest_framework import serializers

from products.models import Product, Category, Image


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'content', 'categories', ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', ]


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['alt', 'image', ]
