# from django.http import response
from django.test import TestCase
from django.urls import reverse,resolve
from .views import cart,shipped,wallet

# Create your tests here.

class Testmasterview(TestCase):

    def test_cart(self):
        res= resolve(reverse("cart"))
        response = self.client.get(reverse("cart"))
        self.assertEqual(200,response.status_code)
        self.assertEqual(response.content,b"CHECK YOUR CART TO KNOW ITEMS FOR PURCHASE")
        self.assertEqual(res.func,cart)

    def test_shipped(self):
        res= resolve(reverse("shipped"))
        response = self.client.get(reverse("shipped"))
        self.assertEqual(200,response.status_code)
        self.assertEqual(response.content,b"GOODS BEING SHIPPED ARE HERE")
        self.assertEqual(res.func,shipped)    

    def test_wallet(self):
        res= resolve(reverse("wallet"))
        response = self.client.get(reverse("wallet"))
        self.assertEqual(200,response.status_code)
        self.assertEqual(response.content,b"WALLET SHOWS ALL YOUR FUNDS")
        self.assertEqual(res.func,wallet)