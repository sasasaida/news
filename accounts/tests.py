from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
class UsersMangersTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username ='test',
            email = 'test@example.com',
            password = 'testpass123',
        )
        self.assertEqual(user.username,'test')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username ='testsuperuser',
            email = 'testsuper@example.com',
            password = 'testpass123',
        )
        self.assertEqual(admin_user.username,'testsuperuser')
        self.assertEqual(admin_user.email, 'testsuper@example.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)