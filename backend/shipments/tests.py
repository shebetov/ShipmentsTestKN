from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from mixer.backend.django import mixer
from .models import City, Shipment


class ShipmentViewSetTest(APITestCase):

    def setUp(self):
        self.url = reverse('shipment-list')

    def test_create_shipment(self):
        data = {
            'city': City.objects.all().first().id,
            'address': 'Test address',
            'status': Shipment.ShipmentStatus.PENDING,
            'comment': 'Test shipment',
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['city'], data['city'])
        self.assertEqual(response.data['address'], data['address'])
        self.assertEqual(response.data['status'], data['status'])
        self.assertEqual(response.data['comment'], data['comment'])

        shipment = Shipment.objects.get(pk=response.data['id'])
        self.assertEqual(shipment.city.id, data['city'])
        self.assertEqual(shipment.address, data['address'])
        self.assertEqual(shipment.status, data['status'])
        self.assertEqual(shipment.comment, data['comment'])

    def test_update_shipment(self):
        shipment = mixer.blend(Shipment)

        before_data = {
            'city': shipment.city.id,
            'address': shipment.address,
            'status': shipment.status,
            'comment': shipment.comment,
        }

        update_data = {
            'status': Shipment.ShipmentStatus.IN_TRANSIT,
            'comment': 'Updated shipment',
        }

        url = reverse('shipment-detail', kwargs={'pk': shipment.id})
        response = self.client.patch(url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['city'], before_data['city'])
        self.assertEqual(response.data['address'], before_data['address'])
        self.assertEqual(response.data['status'], update_data['status'])
        self.assertEqual(response.data['comment'], update_data['comment'])

        shipment.refresh_from_db()
        self.assertEqual(shipment.city.id, before_data['city'])
        self.assertEqual(shipment.address, before_data['address'])
        self.assertEqual(shipment.status, update_data['status'])
        self.assertEqual(shipment.comment, update_data['comment'])
