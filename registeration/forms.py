from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Userdetails, Phonenumbers
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone = forms.NumberInput()
   
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','first_name']

class UserMyForm(forms.ModelForm):
    
    class Meta: 
        model = User
        fields = ['username', 'email', 'first_name']


class UserupForm(forms.ModelForm):
    email = forms.EmailField()
    #hello = forms.TextInput()

    class Meta: 
        model = User
        fields = ['username', 'email']        

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['background_image','image', 'bio']


class Userupdateform(forms.ModelForm):
    class Meta:
        model = Userdetails
        fields = ['dropcountry']  

class Phone(forms.ModelForm):
    class Meta:
        model = Phonenumbers
        fields = ['day','month']          
        
class Birthday(forms.ModelForm):
    class Meta:
        model = Phonenumbers
        fields = ['day','month']          


#class Userupdateformtwo(forms.ModelForm):
 #   class Meta:
  #      model = Userdetailstwo
   #     fields = ['country', 'continent']        

