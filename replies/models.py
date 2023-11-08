from django.db import models
from django.contrib.auth.models import User
from tweets.models import Tweet
# Create your models here.

class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=288)
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content