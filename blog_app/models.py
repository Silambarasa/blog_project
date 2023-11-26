from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    #it will automatically redirect to the URL 
    #defined by the 'home' path name.
    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255,default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(blank=False, null=False, default="")
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255,default="")
    

    #how I would define the str method to return the author and title of a post

    def __str__(self):
        return f"{self.author} - {self.title}"  

    def get_absolute_url(self):
        #return reverse('article-details',args=(str(self.id)))
        return reverse('home')