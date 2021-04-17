from django.contrib import admin
from .models import Profile, Userdetails, Phonenumbers

 #Register your models here.
admin.site.register(Profile)
admin.site.register(Userdetails)
admin.site.register(Phonenumbers)

