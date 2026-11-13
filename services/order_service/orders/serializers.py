from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order

        fields = [
            "order_id",
            "account_id",
            "ticker",
            "side",
            "quantity",
            "limit_price",
            "status",
            "created_at",
        ]

        read_only_fields = [
            "order_id",
            "status",
            "created_at",
        ]

    def validate_ticker(self, value):
        return value.strip().upper()

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Quantity must be greater than zero."
            )

        return value

    def validate_limit_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Limit price must be positive."
            )

        return value