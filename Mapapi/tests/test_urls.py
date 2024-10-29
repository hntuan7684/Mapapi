from django.test import TestCase
from django.urls import reverse, resolve
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from Mapapi.views import (
    NotificationViewSet, UserActionView, get_csrf_token, GetTokenByMailView,
    UserRegisterView, UserAPIListView, UserRetrieveView, IncidentByZoneAPIView,
    IncidentAPIView, IncidentAPIListView, HandleIncidentView, IncidentUserView
)   

class UrlsTestCase(TestCase):
    def test_schema_url(self):
        url = reverse('schema')
        self.assertEqual(resolve(url).func.view_class, SpectacularAPIView)

    def test_swagger_ui_url(self):
        url = reverse('swagger-ui')
        self.assertEqual(resolve(url).func.view_class, SpectacularSwaggerView)

    def test_redoc_url(self):
        url = reverse('redoc')
        self.assertEqual(resolve(url).func.view_class, SpectacularRedocView)

    def test_login_url(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, TokenObtainPairView)

    def test_token_obtain_pair_url(self):
        url = reverse('token_obtain_pair')
        self.assertEqual(resolve(url).func.view_class, TokenObtainPairView)

    def test_token_verify_url(self):
        url = reverse('token_verify')
        self.assertEqual(resolve(url).func.view_class, TokenVerifyView)

    def test_token_refresh_url(self):
        url = reverse('token_refresh')
        self.assertEqual(resolve(url).func.view_class, TokenRefreshView)

    def test_get_csrf_token_url(self):
        url = reverse('get_csrf_token')
        self.assertEqual(resolve(url).func, get_csrf_token)


    def test_get_token_by_mail_url(self):
        url = reverse('get_token_by_mail')
        self.assertEqual(resolve(url).func.view_class, GetTokenByMailView)

    def test_register_url(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, UserRegisterView)

    def test_user_list_url(self):
        url = reverse('user_list')
        self.assertEqual(resolve(url).func.view_class, UserAPIListView)

    def test_user_retrieve_url(self):
        url = reverse('user_retrieve')
        self.assertEqual(resolve(url).func.view_class, UserRetrieveView)

    def test_incident_zone_url(self):
        url = reverse('incidentZone', args=[1])
        self.assertEqual(resolve(url).func.view_class, IncidentByZoneAPIView)

    def test_incident_rud_url(self):
        url = reverse('incident_rud', args=[1])
        self.assertEqual(resolve(url).func.view_class, IncidentAPIView)

    def test_incident_list_url(self):
        url = reverse('incident')
        self.assertEqual(resolve(url).func.view_class, IncidentAPIListView)

    # Add more tests for other URL patterns...

    def test_notification_url(self):
        url = reverse('notification')
        self.assertEqual(resolve(url).func.cls, NotificationViewSet)


    def test_handle_incident_url(self):
        url = reverse('handle', args=[1])
        self.assertEqual(resolve(url).func.view_class, HandleIncidentView)

    def test_user_action_url(self):
        url = reverse('user_action')
        resolved = resolve(url)
        self.assertEqual(resolved.func.cls, UserActionView)


    def test_incident_detail_url(self):
        url = reverse('incident_detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, IncidentUserView)
