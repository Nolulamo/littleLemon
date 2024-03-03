from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from reservation.models import Menu
from reservation.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='nolu', password='nolu123456789')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.menu_item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.menu_item1 = Menu.objects.create(title="Pizza", price=120, inventory=50)

    def test_getall(self):
        url = reverse('menu')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serialized_data = MenuItemSerializer([self.menu_item, self.menu_item1], many=True).data
        self.assertEqual(response.data, serialized_data)

    def test_getall_unauthorized_user(self):
        self.client.logout()
        url = reverse('menu')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
