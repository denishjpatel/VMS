""" purchases URLs"""
from django.urls import path
from .views import PurchaseOrderListCreate, PurchaseOrderRetrieveUpdateDestroy, PurchaseOrderAcknowledge

urlpatterns = [
    path('', PurchaseOrderListCreate.as_view(), name='purchase-order-list-create'),
    path('<int:pk>/', PurchaseOrderRetrieveUpdateDestroy.as_view(), name='purchase-order-retrieve-update-destroy'),
    path('<int:po_id>/acknowledge', PurchaseOrderAcknowledge.as_view(), name='purchase_order_acknowledge'),
]