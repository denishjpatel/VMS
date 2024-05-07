""" Vendors URLs"""
from django.urls import path
from .views import VendorListCreate, VendorRetrieveUpdateDestroy, VendorPerformance

urlpatterns = [
    path('', VendorListCreate.as_view(), name='vendor-list-create'),
    path('<int:pk>/', VendorRetrieveUpdateDestroy.as_view(), name='vendor-retrieve-update-destroy'),
    path('<int:vendor_id>/performance/', VendorPerformance.as_view(), name='vendor-performance'),
]
