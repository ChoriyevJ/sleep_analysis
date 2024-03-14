from django.shortcuts import render
from django.db import models
from django.db.models import functions
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.views import APIView

from shop.models import Category, Brand, Product
from shop import serializers
from shop.cart import Cart


class ProductListAPI(generics.ListAPIView, mixins.CreateModelMixin):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductListSerializer


class ProductDetailAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductListSerializer


class CartAPI(APIView):

    def get(self, request):
        cart = Cart(request)

        return Response(cart)






