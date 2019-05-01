from django.db import models
from django.urls import reverse
from datetime import date
import datetime

# Create your models here.

class Blogger(models.Model):
    biography = models.TextField(max_length = 500, help_text = 'Enter blogger biography')
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    
    date_of_birth = models.DateField('Born', null = True, blank = True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse ('blogger-detail', args = [str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
class Theme(models.Model):
    name = models.CharField(max_length = 200, help_text = 'Enter a theme for your post')

class Language(models.Model):
    name = models.CharField(max_length = 200, help_text = 'Please select the language(s) your post is written in')
    
class Blog(models.Model):
    title = models.CharField(max_length = 100)
    postdate = models.DateField('Post date', auto_now_add=True, null = True, blank = True)
    blogger = models.ForeignKey(Blogger, on_delete = models.SET_NULL, null = True)
    theme = models.ManyToManyField(Theme, help_text = 'Please select a theme for your post')
    content = models.TextField(max_length = 3000, help_text = 'Type your post here')
    language = models.ManyToManyField(Language, help_text = 'Select the content language(s)')
    

    class Meta:
        ordering = ['-postdate']

    def get_absolute_url(self):
        return reverse ('blog-detail', args = [str(self.id)])

    def __str__(self):
        return self.title

from django.contrib.auth.models import User

class BlogInstance(models.Model):
    favblog = models.ForeignKey(User, on_delete = models.SET_NULL, null=True, blank = True)
