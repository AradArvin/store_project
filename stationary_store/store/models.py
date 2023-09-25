from django.db import models
from accounts.models import CustomUser
from django.utils.translation import gettext_lazy as _
# Create your models here.



class Order(models.Model):

    class Status(models.TextChoices):
        PENDING = "P", _("Pending")
        BAN = "B", _("Banned")
        CONFIRM = "C", _("Confirmed")


    customer_id = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=Status.choices, default="P")



class Category(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='category', null=True, blank=True)

    def __str__(self) -> str:
        return self.name



class Items(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='items', null=True, blank=True)
    is_available = models.BooleanField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name




class OrderItem(models.Model):
    item_id = models.ForeignKey(Items, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)




class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order_items = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(default=False)
