"""purchases Views"""
from rest_framework import generics
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer, UpdatePurchaseOrderSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class PurchaseOrderListCreate(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class PurchaseOrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PurchaseOrder.objects.all()
    serializer_class = UpdatePurchaseOrderSerializer


class PurchaseOrderAcknowledge(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, po_id):
        try:
            purchase_order = PurchaseOrder.objects.get(id=po_id)
            purchase_order.acknowledgment_date = timezone.now()
            purchase_order.save()
            return Response({'status': 'acknowledged'}, status=status.HTTP_200_OK)
        except PurchaseOrder.DoesNotExist:
            return Response({'error': 'Purchase Order not found'}, status=status.HTTP_404_NOT_FOUND)
