from uuid import uuid4

from shared.event_contracts.order_events import (
    OrderCreatedData,
    OrderCreatedEvent,
)


def test_order_created_event():

    order_id = uuid4()

    data = OrderCreatedData(
        order_id=order_id,
        account_id="ACC001",
        ticker="AAPL",
        side="BUY",
        quantity=10,
        limit_price="200.00",
    )

    event = OrderCreatedEvent(data=data)

    assert event.event_type == "OrderCreated"
    assert event.schema_version == 1
    assert event.data.order_id == order_id

    print(event.model_dump(mode="json"))