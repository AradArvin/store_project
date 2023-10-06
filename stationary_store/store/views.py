from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404

from .permissions import IsOwnerOrReadOnly
from .models import Category, Items, Order, OrderItem
from .serializers import *

# Create your views here.


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response(
            {
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "count": self.page.paginator.count,
                "total_pages": self.page.paginator.num_pages,
                "results": data,
            }
        )



class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]
    pagination_class = CustomPagination



class ItemsAPIView(generics.ListAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
    permission_classes = [AllowAny,]
    filter_backends = [filters.SearchFilter,]
    search_fields = ["name", "description"]
    pagination_class = CustomPagination


class ShoppingCartAPIView(APIView):

    def get_cart(self, request):
        cart = request.session.get("cart", [])

        cart_details = []
        total_price = 0

        for item in cart:
            product = get_object_or_404(Items, pk=item["item_id"])
            quantity = item["quantity"]
            item_total = product.price * quantity
            total_price += item_total

            cart_details.append(
                {
                    "item": ItemsSerializer(product).data,
                    "quantity": quantity,
                    "item_total": item_total,
                }
            )

        return cart_details, total_price


    def get(self, request):
        cart_details, total_price = self.get_cart(request)
        return Response({"cart_items": cart_details, "total_price": total_price})


    def post(self, request):
        item_id = request.data.get("item_id")
        quantity = int(request.data.get("quantity", 1))

        product = get_object_or_404(Items, pk=item_id)

        cart = request.session.get("cart", [])

        for item in cart:
            if item["item_id"] == item_id:
                item["quantity"] += quantity
                request.session.modified = True
                cart_details, total_price = self.get_cart(request)
                return Response(
                    {"cart_items": cart_details, "total_price": total_price}
                )

        cart.append({"item_id": item_id, "quantity": quantity})
        request.session["cart"] = cart
        request.session.modified = True

        cart_details, total_price = self.get_cart(request)
        return Response({"cart_items": cart_details, "total_price": total_price})


    def delete(self, request):
        item_id = request.data.get("item_id")

        cart = request.session.get("cart", [])

        for item in cart:
            if item["item_id"] == item_id:
                cart.remove(item)
                request.session.modified = True
                cart_details, total_price = self.get_cart(request)
                return Response(
                    {"cart_items": cart_details, "total_price": total_price}
                )

        return Response(status=status.HTTP_404_NOT_FOUND)