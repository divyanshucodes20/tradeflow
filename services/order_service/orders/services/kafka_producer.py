import json
import logging

from confluent_kafka import Producer
from django.conf import settings

logger = logging.getLogger(__name__)

producer = Producer({
    "bootstrap.servers": "localhost:9092",
    "client.id": "tradeflow-order-service",
})


def publish_order_created(order):

    event = {
        "event_id": str(order.order_id),
        "event_type": "OrderCreated",
        "account_id": order.account_id,
        "occurred_at": order.created_at.isoformat(),

        "data": {
            "order_id": str(order.order_id),
            "account_id": order.account_id,
            "ticker": order.ticker,
            "side": order.side,
            "quantity": order.quantity,
            "limit_price": str(order.limit_price),
        }
    }

    delivery_errors = []

    def delivery_report(err, message):
        if err is not None:
            delivery_errors.append(err)
            logger.error("Kafka delivery failed: %s", err)
        else:
            logger.info(
                "Event delivered: topic=%s partition=%s offset=%s",
                message.topic(),
                message.partition(),
                message.offset(),
            )

    producer.produce(
        topic="orders.created",
        key=order.account_id.encode("utf-8"),
        value=json.dumps(event).encode("utf-8"),
        callback=delivery_report,
    )

    remaining = producer.flush(timeout=10)

    if remaining > 0:
        raise TimeoutError("Kafka message delivery timed out")

    if delivery_errors:
        raise RuntimeError(
            f"Kafka delivery failed: {delivery_errors[0]}"
        )

    return event