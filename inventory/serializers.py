from rest_framework import serializers

from .models import PurchaseOrder


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ['product', 'quantity', 'price', 'created_at']

    def create(self, validated_data):
        product = validated_data['product']
        quantity = validated_data['quantity']
        price = validated_data['price']

        # Update the product stock by adding the purchased quantity
        product.stock += quantity
        product.save()

        # Create the purchase order with the calculated price
        purchase_order = PurchaseOrder.objects.create(
            product=product,
            quantity=quantity,
            price=price
        )
        return purchase_order
