from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *



router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'items', ItemsViewSet, basename='item')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'orderitems', OrderItemViewSet, basename='orderitem')



urlpatterns = [
    path('', include(router.urls)),
]