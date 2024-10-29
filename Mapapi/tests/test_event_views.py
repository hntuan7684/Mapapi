# from rest_framework.test import APITestCase
# from django.urls import reverse
# from django.contrib.auth import get_user_model
# from Mapapi.models import Evenement, Zone
# from rest_framework import status

# User = get_user_model()

# class EventViewTests(APITestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(email='test@example.com', password='password')
#         self.client.force_authenticate(user=self.user)
#         self.event = Evenement.objects.create(
#             title='Test Event',
#             zone='Test Zone',
#             description='Test Description',
#             date='2023-05-01T00:00:00Z',
#             lieu='Test Location',
#             user_id=self.user,
#             latitude='0.0',
#             longitude='0.0'
#         )

#     def test_event_list_view(self):
#         url = reverse('event')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn('results', response.data)
#         self.assertEqual(len(response.data['results']), 1)

#     def test_create_event(self):
#         url = reverse('event')
#         data = {
#             'title': 'New Event',
#             'description': 'New Description',
#             'date': '2023-06-01',
#             'user_id': self.user.id,
#             'zone': self.zone.id
#         }
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Evenement.objects.count(), 2)
#         self.assertEqual(response.data['title'], 'New Event')

#     def test_event_detail_view(self):
#         url = reverse('event', args=[self.event.id])
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['title'], 'Test Event')

#     def test_update_event(self):
#         url = reverse('event', args=[self.event.id])
#         data = {
#             'title': 'Updated Event',
#             'description': 'Updated Description',
#             'date': '2023-07-01',
#             'user_id': self.user.id,
#             'zone': self.zone.id
#         }
#         response = self.client.put(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.event.refresh_from_db()
#         self.assertEqual(self.event.title, 'Updated Event')

#     def test_delete_event(self):
#         url = reverse('event', args=[self.event.id])
#         response = self.client.delete(url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Evenement.objects.count(), 0)

