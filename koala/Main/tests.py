# from django.http import response
from django.test import TestCase
from django.urls import reverse,resolve
from.views import about_us, contact_us, home_page
# Create your tests here.

class Viewstestcase(TestCase):


    # def test_home_page(self):
    #     res= resolve(reverse("home"))
    #     response = self.client.get(reverse("home"))
    #     self.assertEqual(200,response.status_code)
    #     self.assertEqual(response.content, b"THIS IS MY WORK")
    #     self.assertEqual(res.func, home_page)

    def test_home_view(self):
        res= resolve(reverse("home"))
        response = self.client.get(reverse("home"))
        self.assertEqual(200,response.status_code)
        self.assertContains(response, "Welcome to Sensei Kido World!")
        self.assertEqual(res.func, home_page)
        self.assertTemplateUsed(response,'home.html')
        self.assertTemplateUsed(response,'base.html')

    def test_contact_view(self):
        res= resolve(reverse("contact"))
        response = self.client.get(reverse("contact"))
        self.assertEqual(200,response.status_code)
        self.assertContains(response,"LinkedIn")
        self.assertEqual(res.func, contact_us)
        self.assertTemplateUsed(response,'contact.html')
        self.assertTemplateUsed(response,'base.html')
        # test for static
        self.assertContains(response, 'ecommerce.css')
        
    def test_about_view(self):
        res= resolve(reverse("about"))
        response = self.client.get(reverse("about"))
        self.assertEqual(200,response.status_code)
        self.assertContains(response,"Lorem ipsum dolor sit amet, consectetur adipisicing elit")
        self.assertEqual(res.func, about_us)
        self.assertTemplateUsed(response,'about.html')
        self.assertTemplateUsed(response,'base.html')
        



    # def test_login(self):
    #     res= resolve(reverse("login"))
    #     response = self.client.get(reverse("login"))
    #     self.assertEqual(200,response.status_code)
    #     self.assertEqual(response.content, b"LOGIN HERE WITH USERNAME AND PASSWORD")
    #     self.assertEqual(res.func, login)

    # def test_account(self):
    #     res= resolve(reverse("account"))
    #     response = self.client.get(reverse("account"))
    #     self.assertEqual(200,response.status_code)
    #     self.assertEqual(response.content, b"VARIOUS ACCOUNTS CAN BE VIEWED HERE")
    #     self.assertEqual(res.func, account)

         