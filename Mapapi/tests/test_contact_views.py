from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from Mapapi.models import Contact, User

class ContactViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', password='password')
        self.client.force_authenticate(user=self.user)
        self.contact = Contact.objects.create(
            objet="Test Contact",
            message="This is a test message",
            email="test@example.com"
        )

    def test_contact_list_view(self):
        url = reverse('contact')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)

    def test_contact_detail_view(self):
        url = reverse('contact', args=[self.contact.id])  # Updated to match the correct URL configuration
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['objet'], 'Test Contact')

    def test_create_contact(self):
        url = reverse('contact')
        data = {
            'objet': 'New Contact',
            'message': 'This is a new test message',
            'email': 'newtest@example.com'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Contact.objects.count(), 2)
        self.assertEqual(response.data['objet'], 'New Contact')
