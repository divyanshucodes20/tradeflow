import uuid

from django.db import models


class Order(models.Model):

    class Side(models.TextChoices):
        BUY = "BUY", "Buy"
        SELL = "SELL", "Sell"

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        ACCEPTED = "ACCEPTED", "Accepted"
        EXECUTED = "EXECUTED", "Executed"
        REJECTED = "REJECTED", "Rejected"

    order_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    account_id = models.CharField(max_length=50)

    ticker = models.CharField(max_length=20)

    side = models.CharField(
        max_length=4,
        choices=Side.choices
    )

    quantity = models.PositiveIntegerField()

    limit_price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ticker} - {self.side} - {self.order_id}"