from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from employee.views import EmployeeViewSet


router = DefaultRouter()
router.register(r'employee', EmployeeViewSet, basename='employee')



urlpatterns = [
    path('', include(router.urls)),
    path('api/categories', CategoryAPIView.as_view(), name='categories'),
    path('api/items', ItemsAPIView.as_view(), name='items'),
    path('api/cart', ShoppingCartAPIView.as_view(), name='cart'),
]