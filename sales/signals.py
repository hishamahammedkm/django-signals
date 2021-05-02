from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Sales
from orders.models import Order
@receiver(pre_delete,sender=Sales)
def order_status(sender,instance,**kwargs):
    obj = instance.order
    obj.active = False
    obj.save()
