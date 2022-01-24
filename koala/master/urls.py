from django.urls import path
from.views import cart,shipped,wallet


urlpatterns = [
    path('cart/',cart, name="cart"),
    path('shipped/',shipped, name="shipped"),
    path('wallet/',wallet, name="wallet"),
]