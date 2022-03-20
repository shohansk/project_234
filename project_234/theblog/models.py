


from ast import mod
import profile
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime , date
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
        
    
    def get_absolute_url(self):
        #return reverse("article-detail", kwargs={"pk": self.pk})
        return reverse("home")

class Post(models.Model):
    title = models.CharField( max_length=250)
    thumbnail = models.ImageField(upload_to = "files/thumbnail",null = True)
    title_tag = models.CharField( max_length=250 )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #body = models.TextField()
    body = RichTextField(blank = True ,null =True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255 )
    likes = models.ManyToManyField(User, related_name='blog_posts')
    snippet = models.CharField(max_length=255)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        #return reverse("article-detail", kwargs={"pk": self.pk})
        return reverse("home")


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments" ,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title ,self.name )


class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to = "files/profile_pic",null = True)
    website_link = models.CharField( max_length=250,null=True,blank=True)
    facebook_link = models.CharField( max_length=250,null=True,blank=True)
    youtube_link = models.CharField( max_length=250,null=True,blank=True)
    instagram_link = models.CharField( max_length=250,null=True,blank=True)
    twitter_link = models.CharField( max_length=250,null=True,blank=True)
    reddit_link = models.CharField( max_length=250,null=True,blank=True)

    def __str__(self):
        return str(self.user)

    
    

   
     
    