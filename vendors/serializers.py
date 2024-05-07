"""Vendors Serializers"""
from rest_framework import serializers
from .models import Vendor, HistoricalPerformance


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

      
class UpdateVendorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    contact_details = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    vendor_code = serializers.CharField(required=False)
    class Meta:
        model = Vendor
        fields = '__all__'


class VendorPerformanceSerializer(serializers.ModelSerializer):
    date = serializers.DateField(required=False)  # Make date optional

    class Meta:
        model = HistoricalPerformance
        fields = ('on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate', 'date')


class VendorPerformanceAggregateSerializer(serializers.Serializer):
    on_time_delivery_rate = serializers.FloatField()
    quality_rating_avg = serializers.FloatField()
    average_response_time = serializers.FloatField()
    fulfillment_rate = serializers.FloatField()