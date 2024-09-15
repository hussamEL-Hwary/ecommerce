from rest_framework import serializers

from products.models import Product


# Base serializer for shared fields and common logic
class ProductBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'sku']


class ProductCreateReadSerializer(ProductBaseSerializer):
    class Meta(ProductBaseSerializer.Meta):
        fields = ProductBaseSerializer.Meta.fields + ['stock']

    def validate_sku(self, value):
        """
        Validate that the SKU is unique and not used by any other product.
        """

        if Product.objects.filter(sku=value).exists():
            raise serializers.ValidationError("This SKU is already in use by another product.")
        return value


class ProductUpdateSerializer(ProductBaseSerializer):
    """Stock should be updated only via sales and purchase."""
    pass
