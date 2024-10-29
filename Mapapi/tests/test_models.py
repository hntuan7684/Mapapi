from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse, resolve

from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from Mapapi.models import (
    Category, Incident, Zone, User, Indicateur,
    Evenement, Contact, Communaute, Rapport,
    Participate, 
)



User = get_user_model()

class UserModelTest(TestCase):
    def test_create_user(self):
        email = 'test@example.com'
        password = 'testpass123'
        user = User.objects.create_user(email=email, password=password)
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)

    def test_create_superuser(self):
        email = 'admin@example.com'
        password = 'adminpass123'
        user = User.objects.create_superuser(email=email, password=password)
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category", description="Test Description")

    def test_category_creation(self):
        self.assertTrue(isinstance(self.category, Category))
        self.assertEqual(self.category.name, "Test Category")
        self.assertTrue(timezone.now() - self.category.created_at < timezone.timedelta(seconds=1))

    def test_category_str_method(self):
        self.assertEqual(str(self.category), "Test Category ")

    def test_category_photo_upload(self):
        file_content = b"This is a test image content"
        test_image = SimpleUploadedFile("test_image.jpg", file_content, content_type="image/jpeg")
        category_with_photo = Category.objects.create(
            name="Category with Photo",
            photo=test_image
        )
        self.assertTrue(category_with_photo.photo)
        self.assertIn("test_image", category_with_photo.photo.name)

class IncidentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.user = User.objects.create(email='test@example.com', first_name='Test', last_name='User')
        cls.category = Category.objects.create(name='Test Category', description='Test Description')
        cls.indicateur = Indicateur.objects.create(name='Test Indicateur')

    def test_create_incident(self):
        incident = Incident.objects.create(
            title='Test Incident',
            zone='Test Zone',
            user_id=self.user,
            category_id=self.category,
            indicateur_id=self.indicateur
        )
        self.assertTrue(isinstance(incident, Incident))
        self.assertEqual(incident.__str__(), 'Test Zone ')

    def test_incident_fields(self):
        incident = Incident.objects.create(
            title='Test Incident',
            zone='Test Zone',
            description='Test Description',
            lattitude='123.456',
            longitude='789.012',
            etat='declared',
            user_id=self.user,
            category_id=self.category,
            indicateur_id=self.indicateur
        )
        self.assertEqual(incident.title, 'Test Incident')
        self.assertEqual(incident.zone, 'Test Zone')
        self.assertEqual(incident.description, 'Test Description')
        self.assertEqual(incident.lattitude, '123.456')
        self.assertEqual(incident.longitude, '789.012')
        self.assertEqual(incident.etat, 'declared')

    def test_incident_relationships(self):
        incident = Incident.objects.create(
            title='Test Incident',
            zone='Test Zone',
            user_id=self.user,
            category_id=self.category,
            indicateur_id=self.indicateur
        )
        self.assertEqual(incident.user_id, self.user)
        self.assertEqual(incident.category_id, self.category)
        self.assertEqual(incident.indicateur_id, self.indicateur)

    def test_incident_created_at(self):
        incident = Incident.objects.create(
            title='Test Incident',
            zone='Test Zone',
            user_id=self.user
        )
        self.assertTrue(abs(incident.created_at - timezone.now()) < timezone.timedelta(seconds=1))

    def test_incident_category_ids(self):
        incident = Incident.objects.create(
            title='Test Incident',
            zone='Test Zone',
            user_id=self.user
        )
        category2 = Category.objects.create(name='Test Category 2', description='Test Description 2')
        incident.category_ids.add(self.category, category2)
        self.assertEqual(incident.category_ids.count(), 2)
        self.assertIn(self.category, incident.category_ids.all())
        self.assertIn(category2, incident.category_ids.all())

    def test_incident_taken_by(self):
        taker = User.objects.create(email='taker@example.com', first_name='Taker', last_name='User')
        incident = Incident.objects.create(
            title='Test Incident',
            zone='Test Zone',
            user_id=self.user,
            taken_by=taker
        )
        self.assertEqual(incident.taken_by, taker)

    def test_incident_zone_required(self):
        with self.assertRaises(ValidationError):
            incident = Incident(title='Test Incident', user_id=self.user)
            incident.full_clean()

class EvenementModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.user = User.objects.create(email='event_test@example.com', first_name='Event', last_name='Tester')

    def test_create_evenement(self):
        evenement = Evenement.objects.create(
            title='Test Event',
            zone='Test Zone',
            lieu='Test Location',
            user_id=self.user
        )
        self.assertTrue(isinstance(evenement, Evenement))
        self.assertEqual(evenement.__str__(), 'Test Zone ')

    def test_evenement_fields(self):
        test_date = timezone.now()
        evenement = Evenement.objects.create(
            title='Test Event',
            zone='Test Zone',
            description='Test Description',
            date=test_date,
            lieu='Test Location',
            latitude='123.456',
            longitude='789.012',
            user_id=self.user
        )
        self.assertEqual(evenement.title, 'Test Event')
        self.assertEqual(evenement.zone, 'Test Zone')
        self.assertEqual(evenement.description, 'Test Description')
        self.assertEqual(evenement.date, test_date)
        self.assertEqual(evenement.lieu, 'Test Location')
        self.assertEqual(evenement.latitude, '123.456')
        self.assertEqual(evenement.longitude, '789.012')

    def test_evenement_relationships(self):
        evenement = Evenement.objects.create(
            zone='Test Zone',
            lieu='Test Location',
            user_id=self.user
        )
        self.assertEqual(evenement.user_id, self.user)

    def test_evenement_created_at(self):
        evenement = Evenement.objects.create(
            zone='Test Zone',
            lieu='Test Location',
            user_id=self.user
        )
        self.assertTrue(abs(evenement.created_at - timezone.now()) < timezone.timedelta(seconds=1))

    def test_evenement_required_fields(self):
        with self.assertRaises(ValidationError):
            evenement = Evenement(title='Test Event')
            evenement.full_clean()

        with self.assertRaises(ValidationError):
            evenement = Evenement(zone='Test Zone')
            evenement.full_clean()

    def test_evenement_str_method(self):
        evenement = Evenement.objects.create(
            zone='Test Zone',
            lieu='Test Location',
            user_id=self.user
        )
        self.assertEqual(str(evenement), 'Test Zone ')

class ContactModelTest(TestCase):
    def test_create_contact(self):
        contact = Contact.objects.create(
            objet="Test Contact",
            message="This is a test message",
            email="test@example.com"
        )
        self.assertTrue(isinstance(contact, Contact))
        self.assertEqual(contact.__str__(), 'Test Contact ')

    def test_contact_fields(self):
        contact = Contact.objects.create(
            objet="Test Contact",
            message="This is a test message",
            email="test@example.com"
        )
        self.assertEqual(contact.objet, "Test Contact")
        self.assertEqual(contact.message, "This is a test message")
        self.assertEqual(contact.email, "test@example.com")

    def test_contact_created_at(self):
        contact = Contact.objects.create(objet="Test Contact")
        self.assertTrue(abs(contact.created_at - timezone.now()) < timezone.timedelta(seconds=1))

    def test_contact_required_fields(self):
        with self.assertRaises(ValidationError):
            contact = Contact()
            contact.full_clean()

class CommunauteModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.zone = Zone.objects.create(name="Test Zone", description="Test Zone Description")

    def test_create_communaute(self):
        communaute = Communaute.objects.create(
            name="Test Community",
            zone=self.zone  # Use the Zone instance instead of a string
        )
        self.assertTrue(isinstance(communaute, Communaute))
        self.assertEqual(communaute.__str__(), 'Test Community ')

    def test_communaute_fields(self):
        communaute = Communaute.objects.create(
            name="Test Community",
            zone=self.zone  # Use the Zone instance instead of a string
        )
        self.assertEqual(communaute.name, "Test Community")
        self.assertEqual(communaute.zone, self.zone)

    def test_communaute_created_at(self):
        communaute = Communaute.objects.create(name="Test Community", zone=self.zone)  # Use the Zone instance
        self.assertTrue(abs(communaute.created_at - timezone.now()) < timezone.timedelta(seconds=1))

    def test_communaute_required_fields(self):
        with self.assertRaises(ValidationError):
            communaute = Communaute()
            communaute.full_clean()

class RapportModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(email='rapport_test@example.com', first_name='Rapport', last_name='Tester')
        cls.incident = Incident.objects.create(zone='Test Zone', user_id=cls.user)

    def test_create_rapport(self):
        rapport = Rapport.objects.create(
            details="Test Report",
            incident=self.incident,
            zone="Test Zone",
            user_id=self.user
        )
        self.assertTrue(isinstance(rapport, Rapport))
        self.assertEqual(rapport.__str__(), 'Test Report ')

    def test_rapport_fields(self):
        rapport = Rapport.objects.create(
            details="Test Report",
            type="Test Type",
            incident=self.incident,
            zone="Test Zone",
            user_id=self.user,
            date_livraison="2023-05-01",
            statut="new",
            disponible=True
        )
        self.assertEqual(rapport.details, "Test Report")
        self.assertEqual(rapport.type, "Test Type")
        self.assertEqual(rapport.incident, self.incident)
        self.assertEqual(rapport.zone, "Test Zone")
        self.assertEqual(rapport.user_id, self.user)
        self.assertEqual(rapport.date_livraison, "2023-05-01")
        self.assertEqual(rapport.statut, "new")
        self.assertTrue(rapport.disponible)

    def test_rapport_created_at(self):
        rapport = Rapport.objects.create(details="Test Report", zone="Test Zone", user_id=self.user)
        self.assertTrue(abs(rapport.created_at - timezone.now()) < timezone.timedelta(seconds=1))

    def test_rapport_required_fields(self):
        with self.assertRaises(ValidationError):
            rapport = Rapport()
            rapport.full_clean()

    def test_rapport_file_upload(self):
        file_content = b"This is a test file content"
        test_file = SimpleUploadedFile("test_file.txt", file_content)
        rapport = Rapport.objects.create(
            details="Test Report with File",
            zone="Test Zone",
            user_id=self.user,
            file=test_file
        )
        self.assertTrue(rapport.file.name)  
        self.assertIn("test_file", rapport.file.name) 
        self.assertEqual(rapport.file.read(), file_content)

    def test_rapport_incidents_relationship(self):
        rapport = Rapport.objects.create(details="Test Report", zone="Test Zone", user_id=self.user)
        incident1 = Incident.objects.create(zone='Test Zone 1', user_id=self.user)
        incident2 = Incident.objects.create(zone='Test Zone 2', user_id=self.user)
        rapport.incidents.add(incident1, incident2)
        self.assertEqual(rapport.incidents.count(), 2)
        self.assertIn(incident1, rapport.incidents.all())
        self.assertIn(incident2, rapport.incidents.all())

class ParticipateModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@example.com", first_name="Test", last_name="User")
        self.evenement = Evenement.objects.create(zone="Test Zone")
        self.participate = Participate.objects.create(evenement_id=self.evenement, user_id=self.user)

    def test_participate_creation(self):
        self.assertTrue(isinstance(self.participate, Participate))
        self.assertEqual(self.participate.evenement_id, self.evenement)
        self.assertEqual(self.participate.user_id, self.user)
        self.assertTrue(timezone.now() - self.participate.created_at < timezone.timedelta(seconds=1))

class ZoneModelTest(TestCase):
    def setUp(self):
        self.zone = Zone.objects.create(
            name="Test Zone",
            description="Test Zone Description",
            lattitude="12.345",
            longitude="67.890"
        )

    def test_zone_creation(self):
        self.assertTrue(isinstance(self.zone, Zone))
        self.assertEqual(self.zone.name, "Test Zone")
        self.assertEqual(self.zone.lattitude, "12.345")
        self.assertEqual(self.zone.longitude, "67.890")
        self.assertTrue(timezone.now() - self.zone.created_at < timezone.timedelta(seconds=1))

    def test_zone_str_method(self):
        self.assertEqual(str(self.zone), "Test Zone ")

    def test_zone_photo_upload(self):
        file_content = b"This is a test image content"
        test_image = SimpleUploadedFile("test_image.jpg", file_content, content_type="image/jpeg")
        zone_with_photo = Zone.objects.create(
            name="Zone with Photo",
            photo=test_image
        )
        self.assertTrue(zone_with_photo.photo)
        self.assertIn("test_image", zone_with_photo.photo.name)

class IndicateurModelTest(TestCase):
    def setUp(self):
        self.indicateur = Indicateur.objects.create(name="Test Indicateur")

    def test_indicateur_creation(self):
        self.assertTrue(isinstance(self.indicateur, Indicateur))
        self.assertEqual(self.indicateur.name, "Test Indicateur")
        self.assertTrue(timezone.now() - self.indicateur.created_at < timezone.timedelta(seconds=1))

    def test_indicateur_str_method(self):
        self.assertEqual(str(self.indicateur), "Test Indicateur ")

    def test_indicateur_unique_name(self):
        with self.assertRaises(Exception):  # This will catch any database-related exception
            Indicateur.objects.create(name="Test Indicateur")
