from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from django_countries.fields import CountryField 
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
 # Create your models here.

MONTH_CHOICES = (
    ('january','JANUARY'),
    ('february', 'FEBRUARY'),
    ('march','MARCH'),
    ('april','APRIL'),
    ('may','MAY'),
    ('june','JUNE'),
    ('july','JULY'),
    ('august','AUGUST'),
    ('september','SEPTEMBER'),
    ('october','OCTOBER'),
    ('november','NOVEMBER'),
    ('december','DECEMBER')
)

DAY_CHOICES = (
    ('01','01'),
    ('02', '02'),
    ('03','03'),
    ('04','04'),
    ('05','05'),
    ('06','06'),
    ('07','07'),
    ('08','08'),
    ('09','09'),
    ('10','10'),
    ('11','11'),
    ('12','12'),
    ('13','13'),
    ('14','14'),
    ('15','15'),
    ('16','16'),
    ('17','17'),
    ('18','18'),
    ('19','19'),
    ('20','20'),
    ('21','21'),
    ('22','22'),
    ('23','23'),
    ('24','24'),
    ('25','25'),
    ('26','26'),
    ('27','27'),
    ('28','28'),
    ('29','29'),
    ('30','30'),
    ('31','31')
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image =  models.ImageField(default= 'default.jpg', upload_to ='profile_pics')
    background_image =  models.ImageField(default= 'backimg.jpg', upload_to ='backimg_pics')
    bio = models.TextField()
   
class Userdetails(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    dropcountry = CountryField(default="India")
    
    def get_absolute_url(self):
        return reverse('blog-home')    

class Phonenumbers(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)    
    mobileno = models.IntegerField()
    
    month = models.CharField(max_length=15, choices=MONTH_CHOICES, default='january')
    day = models.CharField(max_length=2, choices=DAY_CHOICES, default='01')

    def get_absolute_url(self):
        return reverse('blog-home')    