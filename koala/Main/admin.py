from django.contrib import admin
from .models import Animal,Contact
# Register your models here.

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):

    list_display = ("name","dob","specie","population",
    "is_extinct","date_created","date_updated")
    list_filter = ("specie","dob","is_extinct")
    list_editable = ["dob","is_extinct"]
    search_fields = ("name","specie")

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','message',)

