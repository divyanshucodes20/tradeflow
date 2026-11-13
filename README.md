# TradeFlow — Architecture Scaffold

This ZIP contains the proposed TradeFlow microservices directory structure.

## Important
This is a **scaffold**, not a copy of your existing Django source code.
Your screenshot showed existing files under `services/order_service/` such as:
- `config/`
- `orders/`
- `manage.py`
- `requirements.txt` (currently at repository root in the screenshot)

Keep those existing files. Merge the folders from this scaffold into your repository; do not replace your existing `config/`, `orders/`, or `manage.py`.

## Current implementation focus
Start with `services/order_service/`.

- `orders/`: Django ORM models and migrations
- `api/`: DRF endpoints and serializers/schemas
- `application/`: use cases and application interfaces
- `domain/`: business rules and domain concepts
- `infrastructure/`: database adapters and Kafka integration

## Consumer placement
The consumer that processes `orders.created` and executes trades belongs to:

`services/trade_service/infrastructure/messaging/consumers/`

It belongs to Trade Service because that service owns the trade-processing responsibility.

## Planned services
- `order_service`: accepts and manages orders
- `trade_service`: consumes order events and executes simulated trades
- `portfolio_service`: maintains holdings
- `notification_service`: sends notifications
- `analytics_service`: computes trading metrics

Each service will eventually have its own Django project, dependencies, database ownership, and deployment lifecycle.

## Python package markers
The `.gitkeep` files preserve empty directories in the ZIP. When adding Python modules, add `__init__.py` to directories that should be Python packages.
