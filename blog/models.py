from django.db import models

# Create your models here.

class blog(models.Model):
  blog_title=models.CharField('What do you want to call your blog?',max_length=100)
  blog_content=models.TextField('Start off with your blog here!',max_length=1000000)
