from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    post_date = models.DateField(auto_now_add=True)
    author  = models.ForeignKey(User, on_delete=CASCADE)
    category = models.ForeignKey(Category, models.SET_NULL, blank=True, null=True)
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)
    snippet = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name="blog_posts")

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def total_likes(self):
        return self.likes.count()
    
    def get_absolute_url(self):
        # return reverse('article-view', args=(str(self.id)))
        return reverse('home')

class Comment(models.Model):
    post  = models.ForeignKey(Post, related_name="comments", on_delete=CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile")
    website_url = models.URLField(null=True, blank=True)
    facebook_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)
    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')