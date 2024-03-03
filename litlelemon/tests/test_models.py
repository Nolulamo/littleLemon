from django.test import TestCase
from reservation.models import Menu

class TestMenu(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        expected_item_str = "IceCream : 80"
        actual_item_str = f"{item.title} : {item.price}"
        self.assertEqual(actual_item_str, expected_item_str)