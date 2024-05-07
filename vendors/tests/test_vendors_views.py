from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from vendors.models import Vendor
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class VendorTests(APITestCase):
    def setUp(self):
        self.vendor = Vendor.objects.create(
            name="Test Vendor",
            contact_details="1234567890",
            address="123 Test St",
            vendor_code="V123"
        )
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_vendor(self):
        url = reverse('vendor-list-create')
        data = {
            'name': 'New Vendor',
            'contact_details': '0987654321',
            'address': '321 New St',
            'vendor_code': 'V321'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vendor.objects.count(), 2)

    def test_retrieve_vendor(self):
        url = reverse('vendor-retrieve-update-destroy', args=[self.vendor.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Vendor')

    def test_update_vendor(self):
        url = reverse('vendor-retrieve-update-destroy', args=[self.vendor.id])
        data = {'name': 'Updated Vendor'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.vendor.refresh_from_db()
        self.assertEqual(self.vendor.name, 'Updated Vendor')

    def test_delete_vendor(self):
        url = reverse('vendor-retrieve-update-destroy', args=[self.vendor.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Vendor.objects.count(), 0)