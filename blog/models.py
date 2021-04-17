from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

TAG_CHOICES = (
    ('news','NEWS'),
    ('politics', 'POLITICS'),
    ('entertainment','ENTERTAINMENT'),
    ('travel','TRAVEL'),
    ('food','FOOD'),
    ('other','OTHER')
)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    likes = models.ManyToManyField(User, related_name= 'blog_posts')
    tags = models.CharField(max_length=30, choices=TAG_CHOICES, default='other')
    blogimage =  models.ImageField(default= 'blog.jpg', upload_to ='media')
    

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk':self.pk})



class Feedback(models.Model):
    comment = models.TextField()
    reciever = models.IntegerField()
    commentater = models.ForeignKey(User, on_delete= models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('blog-home')

