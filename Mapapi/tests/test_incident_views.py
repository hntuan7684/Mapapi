from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from Mapapi.models import Incident, Zone, Category, Collaboration, UserAction
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
from django.utils import timezone
from datetime import timedelta

User = get_user_model()

class IncidentViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', password='password')
        self.client.force_authenticate(user=self.user)
        self.zone, created = Zone.objects.get_or_create(name='Test Zone')  # Ensure no duplicate Zone creation
        self.category = Category.objects.create(name='Test Category')  # Create category before incident
        self.incident = Incident.objects.create(
            title='Test Incident',
            zone=self.zone.name,  # Use the Zone instance
            user_id=self.user,
            description='Test description',
            etat='declared',
            category_id=self.category
        )

    def test_incident_list_view(self):
        url = reverse('incident')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)
        self.assertEqual(len(response.data['results']), 1)

    def test_create_incident(self):
        url = reverse('incident')  # Updated to match the correct URL configuration
        data = {
            'title': 'New Incident',
            'zone': self.zone.name,  # Use the Zone instance
            'user_id': self.user.id,
            'description': 'New description',
            'etat': 'declared',
            'lattitude': '40.7128',
            'longitude': '-74.0060',
            'category_id': self.category.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Incident.objects.count(), 2)
        self.assertEqual(response.data['title'], 'New Incident')


    def test_incident_detail_view(self):
        url = reverse('incident_rud', args=[self.incident.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Incident')

    def test_update_incident(self):
        url = reverse('incident_rud', args=[self.incident.id])
        data = {
            'title': 'Updated Incident',
            'zone': self.zone.id,
            'user_id': self.user.id,
            'description': 'Updated description',
            'etat': 'resolved'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.incident.refresh_from_db()
        self.assertEqual(self.incident.title, 'Updated Incident')
        self.assertEqual(self.incident.etat, 'resolved')

    def test_delete_incident(self):
        url = reverse('incident_rud', args=[self.incident.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Incident.objects.count(), 0)

    def test_incident_filter(self):
        url = reverse('incident_filter')
        response = self.client.get(url, {'filter_type': 'today'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add more assertions based on your filter logic

    # def test_incident_by_zone(self):
    #     url = reverse('incidentZone', args=[self.zone.id])  # Updated to match the correct URL configuration
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data), 1)
    #     self.assertEqual(response.data[0]['title'], 'Test Incident')

class IncidentViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='testuser@example.com', password='testpass123')
        self.zone, created = Zone.objects.get_or_create(name='Test Zone')  # Ensure no duplicate Zone creation
        self.category = Category.objects.create(name='Test Category')
        self.incident = Incident.objects.create(
            title='Test Incident',
            description='Test Description',
            user_id=self.user,
            zone=self.zone.name,  # Use the Zone instance
            category_id=self.category,
            lattitude='40.7128',
            longitude='-74.0060'
        )

    def test_incident_api_list_view(self):
        url = reverse('incident')  # Updated to match the correct URL configuration
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('results' in response.data)

    def test_incident_not_resolved_api_list_view(self):
        url = reverse('incidentNotResolved')  # Updated to match the correct URL configuration
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('results' in response.data)

    def test_incident_on_week_api_list_view(self):
        url = reverse('IncidentOnWeek')  # Updated to match the correct URL configuration
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('data' in response.data)

    def test_incident_search_view(self):
        url = reverse('search')  # Updated to match the correct URL configuration
        response = self.client.get(url, {'search_term': 'Test'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_handle_incident_view(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('handle', args=[self.incident.id])  # Updated to match the correct URL configuration
        response = self.client.post(url, {'action': 'taken_into_account'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.incident.refresh_from_db()
        self.assertEqual(self.incident.etat, 'taken_into_account')


    def test_incident_user_view(self):
        self.client.force_authenticate(user=self.user)
        self.incident.taken_by = self.user
        self.incident.save()
        url = reverse('incident_detail', args=[self.incident.id])  # Updated to match the correct URL configuration
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('user' in response.data)

    # def test_handle_collaboration_request_view(self):
    #     self.client.force_authenticate(user=self.user)
    #     collaboration = Collaboration.objects.create(
    #         user=self.user, 
    #         incident=self.incident,
    #         end_date=timezone.now().date() + timedelta(days=30)  # Set a valid end_date
    #     )
    #     # Ensure collaboration.id is not None
    #     self.assertIsNotNone(collaboration.id, "Collaboration ID should not be None")
        
    #     url = reverse('handle_collaboration_request', args=[collaboration.id, 'accept'])  # Updated to match the correct URL configuration
    #     response = self.client.post(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Add more tests for other views as needed
