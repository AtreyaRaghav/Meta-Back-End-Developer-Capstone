from django.test import TestCase
from Restaurant.models import Menu, Booking
from decimal import Decimal
from datetime import datetime


class MenuTest(TestCase):

    def test_create_item(self):
        item = Menu.objects.create(Title="Cheese Cake", Price=Decimal('80'), Inventory=100)
        self.assertEqual(str(item), "Cheese Cake 80 100")

    def test_default_inventory(self):
        item = Menu.objects.create(Title="Pizza", Price=Decimal('50'), Inventory=5)
        self.assertEqual(item.Inventory, 5)


class BookingTest(TestCase):

    def test_create_booking(self):
        booking = Booking.objects.create(
            Name="Raghav sharma",
            No_of_guests=3,
            BookingDate=datetime(2026, 5, 24, 18, 0)
        )
        expected_str = "Raghav sharma with 3 guests on 2026-05-24 18:00:00"
        self.assertEqual(str(booking), expected_str)

    def test_default_number_of_guests(self):
        booking = Booking.objects.create(
            Name="Jane Doe",
            BookingDate=datetime(2023, 6, 24, 19, 0),
            No_of_guests =3
        )
        self.assertEqual(booking.No_of_guests, 3)