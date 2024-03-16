from rest_framework import serializers

from shop.models import Category, Brand, Product, Cart


class ProductListSerializer(serializers.ModelSerializer):

    brand = serializers.StringRelatedField(source="brand.title")
    category = serializers.StringRelatedField(source="category.title")

    class Meta:
        model = Product
        fields = (
            'title',
            'brand',
            'category',
            'price',
            'image'
        )


class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'title',
            'description',
            'price',
            'image',
        )


class CartSerializer(serializers.ModelSerializer):

    product = ProductDetailSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = (
            'product',
            'quantity'
        )


class CartCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = (
            'product',
            'quantity'
        )





