
from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        "order_id",
        "account_id",
        "ticker",
        "side",
        "quantity",
        "limit_price",
        "status",
        "created_at",
    )

    list_filter = ("side", "status")

    search_fields = ("account_id", "ticker", "order_id")
