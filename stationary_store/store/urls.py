from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from employee.views import EmployeeViewSet


router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'items', ItemsViewSet, basename='item')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'orderitems', OrderItemViewSet, basename='orderitem')
router.register(r'employee', EmployeeViewSet, basename='employee')
router.register(r'carts', CartViewSet, basename='cart')


urlpatterns = [
    path('', include(router.urls)),
]