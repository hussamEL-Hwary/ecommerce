from django.db import models

from customers.models import Customer
from products.models import Product


class SalesOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sales_orders')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='sales_orders')
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SalesOrder #{self.id} - {self.product.name}"
