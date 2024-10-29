from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from Mapapi.models import Zone
from rest_framework import status

User = get_user_model()

class ZoneViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', password='password')
        self.client.force_authenticate(user=self.user)
        self.zone = Zone.objects.create(
            name='Test Zone',
            lattitude='12.345',
            longitude='67.890'
        )

    # def test_zone_list_view(self):
    #     url = reverse('zone_list')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertIn('results', response.data)
    #     self.assertEqual(len(response.data['results']), 1)

    def test_create_zone(self):
        url = reverse('zone_list')
        data = {
            'name': 'New Zone',
            'lattitude': '23.456',
            'longitude': '78.901'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Zone.objects.count(), 2)
        self.assertEqual(response.data['name'], 'New Zone')

    def test_zone_detail_view(self):
        url = reverse('zone', args=[self.zone.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Zone')

    def test_update_zone(self):
        url = reverse('zone', args=[self.zone.id])
        data = {
            'name': 'Updated Zone',
            'lattitude': '34.567',
            'longitude': '89.012'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.zone.refresh_from_db()
        self.assertEqual(self.zone.name, 'Updated Zone')

    def test_delete_zone(self):
        url = reverse('zone', args=[self.zone.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Zone.objects.count(), 0)

