from django.urls import path
from .views import home_page,contact_us,about_us

urlpatterns =[
    path('home/',home_page, name="home"),
    path('contactus/', contact_us, name='contact'),
    path('aboutus/', about_us, name= 'about')
]



