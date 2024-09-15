from rest_framework import serializers

from products.models import Product
from .models import SalesOrder, Customer


class SalesOrderSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True)
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(), write_only=True)

    class Meta:
        model = SalesOrder
        fields = ['product', 'customer', 'quantity', 'created_at']

    def validate(self, data):
        product = data['product']
        quantity = data['quantity']

        # Check if the product has enough stock
        if product.stock < quantity:
            raise serializers.ValidationError("Insufficient stock for this product.")

        return data

    def create(self, validated_data):
        product = validated_data['product']
        customer = validated_data['customer']
        quantity = validated_data['quantity']

        # Calculate the price as quantity * product price
        calculated_price = quantity * product.price

        # Update the product stock
        product.stock -= quantity
        product.save()

        # Create the sales order
        sales_order = SalesOrder.objects.create(
            customer=customer,
            product=product,
            quantity=quantity,
            price=calculated_price
        )
        return sales_order
