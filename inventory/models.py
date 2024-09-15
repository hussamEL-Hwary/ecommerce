from django.db import models
from products.models import Product

class PurchaseOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='purchase_orders')
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"PurchaseOrder #{self.id} - {self.product.name}"
