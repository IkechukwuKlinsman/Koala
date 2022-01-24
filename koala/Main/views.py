import email
from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact

# Create your views here.

def home_page(request):
    return render(request,"home.html")

def contact_us(request):
    if request.method == 'POST':
        # name = request.POST['Name']
        # email = request.POST['E-mail']
        # message = request.POST['Password']
        
        # new = Contact(name= name, email= email, message= message)
        # # new.save()
        # return HttpResponse('Data Saved')
        request_data = dict(request.POST)
        request_data.pop('csrfmiddlewaretoken')
        data = {key:request_data.get(key)[0]
        for key in request_data}
        Contact.objects.create(name= data['Name'], email= data['E-mail'], 
                               message= data['Password'])
        print(data)
        print(data.get("Name"))
        print(request.POST)
    
    return render(request,"contact.html")


def about_us(request):
    return render(request,'about.html')

