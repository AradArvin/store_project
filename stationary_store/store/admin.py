from django.contrib import admin
from .models import Category, Items, Order, OrderItem
# Register your models here.



@admin.register(Category)
class CategoryDisplay(admin.ModelAdmin):
    pass



@admin.register(Items)
class ItemsDisplay(admin.ModelAdmin):
    pass



@admin.register(Order)
class OrderDisplay(admin.ModelAdmin):
    pass



@admin.register(OrderItem)
class OrderItemDisplay(admin.ModelAdmin):
    pass