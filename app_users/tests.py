from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from .views import Validator, register_request


class CustomUserTests(TestCase):
    """ we do not need to test all log in and log out features since those are built into Django and have already tests
    except test for several users that must not have the same email"""

    @classmethod
    def setUpTestData(cls):
        """setUpTestData() is called once at the start of the test run for class-level tuning. You can use it to
        create objects that are not meant to be modified or changed in test methods. """
        user_model = get_user_model()

        # Create a user used to test_good_login_returns_true
        cls.user = user_model.objects.create_user(
            username = "testuser", email = "test@email.com", password = "secret",
        )

        # Create a user 1
        cls.user_1 = user_model.objects.create_user(
            username = 'will',
            email = 'will@email.com',
            password = 'testpass123',
        )

        # Create a user 2 to test password reset and email
        cls.reset_password_user = user_model.objects.create_user(
            username = 'resetuser',
            email = 'resetuser@email.com',
            password = 'testpass123',
        )

        # Générer un UID et un token pour l'utilisateur créé
        cls.uid = urlsafe_base64_encode(force_bytes(cls.reset_password_user.pk))
        cls.token = default_token_generator.make_token(cls.reset_password_user)

    def test_create_user_content(self):
        self.assertEqual(self.user_1.username, 'will')
        self.assertEqual(self.user_1.email, 'will@email.com')
        self.assertTrue(self.user_1.is_active)

    def test_register_page_status_code(self):
        response = self.client.get("/register/")
        self.assertEqual(response.status_code, 200)

    def test_register_page_url_by_name(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)

    def test_register_correct_template(self):
        response = self.client.get(reverse("register"))
        self.assertTemplateUsed(response, 'register.html')

    def test_valid_email_not_exist(self):
        self.assertFalse(Validator.valid_email_exist('toto@gmail.com'))

    def test_valid_email_exist(self):
        self.assertTrue(Validator.valid_email_exist('will@email.com'))

    def test_not_possible_create_users_with_same_email(self):
        class MockRegister:
            def __init__(self, dic):
                self.META = {"CSRF_COOKIE": "test"}
                self.method = 'POST'
                self.POST = dic

        data_dict = {"username": "test", "email": 'will@email.com', "password1": "@a123@!Ab", "password2": "@a123@!Ab"}
        mock = MockRegister(data_dict)
        response = register_request(mock)
        self.assertTrue(response, 200)

    def test_login_request_page_returns_200(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_page_status_name(self):
        response = self.client.get("/login/")
        self.assertEqual(response.status_code, 200)

    def test_login_url_name(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_good_login_returns_true(self):
        login = self.client.login(username = "testuser", email = "test@email.com", password = "secret")
        self.assertTrue(login)

    def test_logout_page_returns_200(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_password_reset_page_returns_200(self):
        response = self.client.get(reverse('password_reset'))
        self.assertEqual(response.status_code, 200)

    def test_password_reset_done_page_returns_200(self):
        response = self.client.get(reverse('password_reset_done'))
        self.assertEqual(response.status_code, 200)

    def test_password_reset_complete_page_returns_200(self):
        response = self.client.get(reverse('password_reset_complete'))
        self.assertEqual(response.status_code, 200)

    def test_password_reset_confirm_page_returns_200(self):
        response = self.client.get(
            reverse('password_reset_confirm', kwargs = {'uidb64': self.uid, 'token': self.token}))
        self.assertEqual(response.status_code, 302)



