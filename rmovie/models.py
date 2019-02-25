from django.db import models
import datetime
from tinymce.models import HTMLField
from django.utils import timezone
from markdown_deux import markdown
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse
from tinymce.models import HTMLField
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username

class Moviee(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=150)
  mdate = models.DateField()
  rating = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
  murl = models.URLField(blank = True, null = True)
  movietime = models.CharField(max_length=50)
  mtype = models.CharField(max_length=100)
  director =  models.CharField(max_length=100)
  quality =  models.CharField(max_length=100,default="HD")
  description =HTMLField()
  maincast = HTMLField()
  body = models.CharField(max_length=200)
  ytube = models.URLField(blank = True, null = True)
  timestamp = models.DateTimeField(auto_now_add=True, null=True)

  def __str__(self):
    return self.name
  
  def __unicode__(self):
    return self.name

  def get_absolute_url(self):
        return reverse('movie-detail', kwargs={
            'id': self.id
        })
    
  def get_update_url(self):
      return reverse('movie-update', kwargs={
          'id': self.id
      })

  def get_delete_url(self):
      return reverse('post-delete', kwargs={
          'id': self.id
      })

  @property
  def get_cast(self):
      return self.comments.all().order_by('-role')

  @property
  def get_link(self):
      return self.link.all().order_by('-role')


class Movie(models.Model):
  name = models.ForeignKey(Moviee, related_name='link', on_delete=models.CASCADE)
  link = models.URLField(default="http://www.watchonlinemovies.com.pk/")
  role = models.CharField(max_length=50)

  def __str__(self):
    return self.link

  def __unicode__(self):
    return self.link

  @property
  def get_link(self):
      return self.link.all().order_by('-role')

  
class Cast(models.Model):
  name = models.ForeignKey(Moviee, related_name='comments', on_delete=models.CASCADE)
  cname = models.CharField(max_length=100)
  cmname = models.CharField(max_length=100)
  role = models.CharField(max_length=50)
  murl = models.URLField(blank = True, null = True)

  def __str__(self):
    return self.cname

  def __unicode__(self):
    return self.cname



class Detai(models.Model):
  name = models.OneToOneField(Moviee, on_delete=models.CASCADE)
  Status = models.CharField(max_length=100)
  Language = models.CharField(max_length=100)
  Budget = models.CharField(max_length=100)
  Revenue = models.CharField(max_length=100)
  Production_Companies = models.CharField(max_length=150)
  Production_Country = models.CharField(max_length=150)
  adult = models.CharField(max_length=10)

  def __str__(self):
    return self.Language
  
  def __unicode__(self):
    return self.Language
