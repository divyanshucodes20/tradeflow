
from datetime import datetime, timezone
from decimal import Decimal
from typing import Literal
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field


class OrderCreatedData(BaseModel):
    """Business data associated with a newly created order."""

    model_config = ConfigDict(extra="forbid")

    order_id: UUID
    account_id: str
    ticker: str
    side: Literal["BUY", "SELL"]
    quantity: int = Field(gt=0)
    limit_price: Decimal = Field(gt=0)


class OrderCreatedEvent(BaseModel):
    """Event published when an order is successfully created."""

    model_config = ConfigDict(extra="forbid")

    event_id: UUID = Field(default_factory=uuid4)

    event_type: Literal["OrderCreated"] = "OrderCreated"

    schema_version: int = 1

    occurred_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    producer: Literal["order-service"] = "order-service"

    data: OrderCreatedData
