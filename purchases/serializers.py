"""purchases Serializers"""
from rest_framework import serializers
from .models import PurchaseOrder


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'


class UpdatePurchaseOrderSerializer(serializers.ModelSerializer):
    po_number = serializers.CharField(required=False)
    order_date = serializers.DateTimeField(required=False)
    delivery_date = serializers.DateTimeField(required=False)
    items = serializers.JSONField(required=False)
    quantity = serializers.IntegerField(required=False)
    status = serializers.ChoiceField(required=False, choices=['pending', 'completed', 'canceled'])
    quality_rating = serializers.FloatField(required=False)
    issue_date = serializers.DateTimeField(required=False)
    acknowledgment_date = serializers.DateTimeField(required=False)

    class Meta:
        model = PurchaseOrder
        fields = '__all__'