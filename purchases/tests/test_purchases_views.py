from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from purchases.models import PurchaseOrder
from vendors.models import Vendor
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class PurchaseOrderTests(APITestCase):
    def setUp(self):
        self.vendor = Vendor.objects.create(
            name="Test Vendor",
            contact_details="1234567890",
            address="123 Test St",
            vendor_code="V123"
        )
        self.purchase_order = PurchaseOrder.objects.create(
            po_number="PO123",
            vendor=self.vendor,
            order_date="2024-01-01T00:00:00Z",
            delivery_date="2024-01-10T00:00:00Z",
            items={"item1": "10", "item2": "20"},
            quantity=30,
            status='pending'
        )
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_purchase_order(self):
        url = reverse('purchase-order-list-create')
        data = {
            'po_number': 'PO321',
            'vendor': self.vendor.id,
            'order_date': '2024-02-01T00:00:00Z',
            'delivery_date': '2024-02-10T00:00:00Z',
            'items': {"item1": "15", "item2": "25"},
            'quantity': 40,
            'status': 'pending'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PurchaseOrder.objects.count(), 2)

    def test_retrieve_purchase_order(self):
        url = reverse('purchase-order-retrieve-update-destroy', args=[self.purchase_order.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['po_number'], 'PO123')

    def test_update_purchase_order(self):
        url = reverse('purchase-order-retrieve-update-destroy', args=[self.purchase_order.id])
        data = {
            'status': 'completed',
            'vendor': self.vendor.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.purchase_order.refresh_from_db()
        self.assertEqual(self.purchase_order.status, 'completed')

    def test_acknowledge_purchase_order(self):
        url = reverse('purchase_order_acknowledge', args=[self.purchase_order.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.purchase_order.refresh_from_db()
        self.assertIsNotNone(self.purchase_order.acknowledgment_date)
    