from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

# PublishedManager only shows published posts.
class PublishedManager(models.Manager):
  def get_queryset(self):
    return super(PublishedManager,self).get_queryset().filter(status='published')

class Post(models.Model):
  # These are the managers, which are a interface through to a database query operation
  objects = models.Manager()
  published = PublishedManager()
  STATUS_CHOICES = (
      ('draft', 'DRAFT'),
      ('published', 'PUBLISHED'),
  )
  # This is field for the post, charfield is a VARCHAR column in SQL
  title = models.CharField(max_length=250)
  # Field to be used by URLs, A slug is a short label that contains only letters, numbers, underscores, or hyphens
  slug = models.SlugField(max_length=250,
                          unique_for_date='publish')
  # Field defines a one to many relationship with USER, cascade stats that if the user is deleted delete all posts,
  # cascaded down.
  author = models.ForeignKey(User, 
                            on_delete=models.CASCADE,
                            related_name='blog_posts')
  # The body of the bost, TEXT column in SQL
  body = models.TextField()
  # Field to state when publised using curent datetime
  publish = models.DateTimeField(default=timezone.now)
  # Field to indicate when created, auto_now_add means the date will be saved automaticaly when creating the object.
  created = models.DateTimeField(auto_now_add=True)
  # Field to indicate when updates, auto_now means the date will be saved automaticaly when updating.
  updated = models.DateTimeField(auto_now=True)
  # Field to show status of post, Published or Draft, default draft. 
  status = models.CharField(max_length=10,
                            choices = STATUS_CHOICES,
                            default='draft')
  # This contains the models meta data, here we state sort by publish in decending order by default when quering the database.
  class Meta:
    ordering = ('-publish',)
  # __str__ is the default humam-readable reprentation of the object.
  def __str__(self):
    return self.title
  def get_absolute_url(self):
    return reverse('blog:post_detail',
                    args= [self.publish.year,
                            self.publish.month,
                            self.publish.day,
                            self.slug])



