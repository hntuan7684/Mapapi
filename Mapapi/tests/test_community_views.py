# from rest_framework.test import APITestCase
# from django.urls import reverse
# from django.contrib.auth import get_user_model
# from Mapapi.models import Communaute
# from rest_framework import status

# User = get_user_model()

# class CommunityViewTests(APITestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(email='test@example.com', password='password')
#         self.client.force_authenticate(user=self.user)
#         self.community = Communaute.objects.create(
#             nom='Test Community',  
#             description_communaute='Test Description'  
#         )

#     def test_community_list_view(self):
#         url = reverse('community')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn('results', response.data)
#         self.assertEqual(len(response.data['results']), 1)

#     def test_create_community(self):
#         url = reverse('community')
#         data = {
#             'name': 'New Community',
#             'description': 'New Description'
#         }
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Communaute.objects.count(), 2)
#         self.assertEqual(response.data['name'], 'New Community')

#     def test_community_detail_view(self):
#         url = reverse('community', args=[self.community.id])
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['name'], 'Test Community')

#     # Add update and delete tests if applicable

