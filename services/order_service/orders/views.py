import logging

from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import OrderSerializer
from .services.kafka_producer import publish_order_created

logger = logging.getLogger(__name__)


class OrderCreateView(APIView):

    def post(self, request):

        serializer = OrderSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        with transaction.atomic():

            order = serializer.save()

            transaction.on_commit(
                lambda: publish_order_created(order)
            )

        return Response(
            {
                "message": "Order created successfully",
                "order": OrderSerializer(order).data,
            },
            status=status.HTTP_201_CREATED
        )