from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserTestS(TestCase):
    def test_create_user(self):
        """Check whether user can be crated using 
        international phone Numbering and password"""
        phone_no = 989111340696
        password = "amitis@123"
        user = User.objects.create_user(
            phone_number=phone_no,
            password=password
        )
        self.assertEqual(user.phone_number, phone_no)
        self.assertTrue(user.check_password(password))