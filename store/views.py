from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from store.models import Product, Category
from store import serializers
from store.cart import Cart


class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductDetailAPI(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductDetailSerializer


class CartAPI(APIView):

    def get(self, request):

        cart = Cart(request)

        return Response(cart.cart)





