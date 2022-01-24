from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cart(request):
    return HttpResponse("CHECK YOUR CART TO KNOW ITEMS FOR PURCHASE")

def shipped(request):
    return HttpResponse("GOODS BEING SHIPPED ARE HERE")

def wallet(request):
    return HttpResponse("WALLET SHOWS ALL YOUR FUNDS")