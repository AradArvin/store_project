from rest_framework import serializers
from .models import Category, Items, Order, OrderItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'
        depth = 2



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        depth = 2


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
        depth = 2