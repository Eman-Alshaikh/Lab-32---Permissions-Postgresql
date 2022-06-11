from re import U
from django.forms import PasswordInput
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

# Create your tests here.

class TestArticleView(TestCase):


    def setUp(self)  :
        self.client.login(username="admin",password="123456")
 
    def test_authentication_required(self):
        self.client.logout()
        url=reverse('articles_list')
        # 403 : forbidden 
        response=self.client.get(url)

        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)