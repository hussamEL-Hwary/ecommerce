from django.db import models
from django.utils.text import slugify
import uuid

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=50, unique=True, blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        # Automatically generate SKU if not provided
        if not self.sku:
            self.sku = self.generate_sku()
        super().save(*args, **kwargs)

    def generate_sku(self):
        # Example SKU generation: using a combination of name slug and a UUID
        # Ensures SKU is unique and human-readable to some extent
        base_sku = slugify(self.name)[:10]  # Slugify the first 10 chars of the product name
        unique_id = uuid.uuid4().hex[:6]    # Add a unique 6-char segment
        return f"{base_sku}-{unique_id}".upper()

    def __str__(self):
        return f"{self.name} ({self.sku})"
