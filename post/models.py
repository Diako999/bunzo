from django.db import models
from django.conf import settings
from django.utils import timezone
import datetime

class Post(models.Model):
    title = models.CharField(max_length = 150)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    tag = models.CharField(max_length = 150)
    published_date = models.DateTimeField(default = timezone.now())
    reading_time = models.IntegerField(blank= True, null = True)
    likes = models.IntegerField(blank= True, null = True)
    comments = models.IntegerField(blank= True, null = True)
    post_detail = models.TextField()


    def __str__(self):
        return self.title
