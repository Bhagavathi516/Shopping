from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.
class UserSignupViewsTest(TestCase):
    def setUp(self):
        self.signup_url = reverse('register')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

    def test_user_signup_view(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/signup.html')

        response = self.client.post(self.signup_url, {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
        })
        self.assertEqual(response.status_code, 302)
        new_user = User.objects.get(username='newuser')
        self.assertEquals(new_user.username, 'newuser')


class UserProfileViewTest(TestCase):
    def setUp(self):
        self.profile_url = reverse('profile')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

    def test_user_profile_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        # self.assertRedirects(response, f'{self.profile_url}') 

    def test_user_profile_view_unauthenticated(self):
        response= self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))


class UserLoginViewTest(TestCase):
    def setUp(self):
        self.login_url = reverse('login')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

    def test_user_login_view(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        response = self.client.post(self.login_url, {
            'username_or_email': 'testuser',
            'password' : 'testpassword',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful login
        self.assertRedirects(response, reverse('item_list'))


class SuperuserViewTest(TestCase):
    def setUp(self):
        self.superuser_url = reverse('admin_view')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

    def test_superuser_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.superuser_url)
        self.assertEqual(response.status_code, 403)  # Forbidden for non-superusers


class CustomPasswordChangeViewTest(TestCase):
    def setUp(self):
        self.password_change_url = reverse('password_change')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.client.login(username='testuser', password='testpassword')


    def test_custom_password_change_view(self):
        response = self.client.get(self.password_change_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(self.password_change_url, {
            'old_password': 'testpassword',
            'new_password1': 'newtestpassword',
            'new_password2': 'newtestpassword',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful password change
        self.assertRedirects(response, reverse('profile'))

        # Log out and try to log in with the new password
        self.client.logout()
        response = self.client.post(reverse('login'), {
            'username_or_email': 'testuser',
            'password': 'newtestpassword',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful login

        # Log in with the old password should now fail
        response = self.client.post(reverse('login'), {
            'username_or_email': 'testuser',
            'password': 'testpassword',
        })
        self.assertNotEqual(response.status_code, 200)  # Login failed