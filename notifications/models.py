from django.db import models

from products.models import Product


class Notification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name}: {self.message}"
