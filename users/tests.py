from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import userProfile

class DocWiseViewsTestCase(TestCase):
    def test_home_page_loads_successfully(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'DocWise')

    def test_about_page_loads_successfully(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Archana Bhade')
        self.assertContains(response, 'Pranay Chandrikapure')

    def test_login_page_loads_successfully(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Member Login')

    def test_register_page_loads_successfully(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Create Account')

    def test_registration_creates_user_and_profile(self):
        registration_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword123',
            'age': 25,
            'income': 300000,
            'cast': 'OPEN',
            'state': 'Maharashtra',
            'profession': 'Student',
            'education_level': 'undergraduate',
            'life_stage': 'student'
        }
        response = self.client.post(reverse('register'), data=registration_data)
        self.assertEqual(response.status_code, 302)  # Redirects to home
        self.assertTrue(User.objects.filter(username='testuser').exists())
        user = User.objects.get(username='testuser')
        self.assertTrue(userProfile.objects.filter(user=user).exists())
        profile = userProfile.objects.get(user=user)
        self.assertEqual(profile.age, 25)
        self.assertEqual(profile.cast, 'OPEN')

    def test_login_workflow(self):
        # Create user
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword123')
        userProfile.objects.create(
            user=user,
            age=25,
            income=300000,
            cast='OPEN',
            state='Maharashtra',
            profession='Student',
            education_level='undergraduate',
            life_stage='student'
        )
        
        login_data = {
            'username': 'testuser',
            'password': 'testpassword123',
            'termsCheck': 'on'
        }
        response = self.client.post(reverse('login'), data=login_data)
        self.assertEqual(response.status_code, 302)  # Redirects to home
        self.assertTrue(response.url.endswith(reverse('home')) or response.url == reverse('home'))

