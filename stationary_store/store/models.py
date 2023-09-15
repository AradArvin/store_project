from django.db import models

# Create your models here.



class Order(models.Model):

    class Status(models.TextChoices):
        PENDING = "P", _("Pending")
        BAN = "B", _("Banned")
        CONFIRM = "C", _("Confirmed")


    customer_id = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=Status.choices, default="P")


