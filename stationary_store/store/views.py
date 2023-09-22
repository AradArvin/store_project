from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.response import Response

from .permissions import IsOwnerOrReadOnly
from .models import Category, Items, Order, OrderItem
from .serializers import *
from .renderers import CartJSONRenderer

# Create your views here.



class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]




class ItemsViewSet(ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]




class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]




class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CartSerializer

    # def post(self, request):
    #     cart = request.data.get('cart', {})
        
    #     serializer = self.serializer_class(data=cart)
    #     serializer.is_valid(raise_exception=True)
        
    #     return Response(serializer.data, status=status.HTTP_200_OK)