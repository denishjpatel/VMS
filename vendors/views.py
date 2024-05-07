"""Vendors Views"""
from rest_framework import generics
from .models import Vendor, HistoricalPerformance
from .serializers import VendorSerializer, VendorPerformanceSerializer, UpdateVendorSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Avg


class VendorListCreate(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = UpdateVendorSerializer


class VendorPerformance(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = HistoricalPerformance.objects.all()
    serializer_class = VendorPerformanceSerializer
    lookup_field = 'vendor_id'


class VendorPerformance(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = HistoricalPerformance.objects.all()
    serializer_class = VendorPerformanceSerializer
    lookup_field = 'vendor_id'

    def get_object(self):
        vendor_id = self.kwargs.get('vendor_id')
        performance_data = self.queryset.filter(vendor_id=vendor_id).aggregate(
            on_time_delivery_rate=Avg('on_time_delivery_rate'),
            quality_rating_avg=Avg('quality_rating_avg'),
            average_response_time=Avg('average_response_time'),
            fulfillment_rate=Avg('fulfillment_rate')
        )
        return performance_data

