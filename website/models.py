from turtle import title
from django.db import models
# Create your models here.
class Thought(models.Model):
    title = models.CharField(max_length = 255)
    thought = models.TextField(max_length = 500)
    thought_link = models.URLField(max_length = 500)
    date_created = models.DateTimeField(auto_now_add = True)


class YoutubeLink (models.Model):
    title = models.CharField(max_length = 255)
    video_link = models.TextField(max_length = 5000)
    date_created = models.DateTimeField(auto_now_add = True)