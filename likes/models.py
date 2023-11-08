from django.db import models
from django.contrib.auth.models import User
from tweets.models import Tweet
# Create your models here.


class Likes(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, related_name="likes", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner','post']

    def __str__(self):
        return f'{self.owner} {self.tweet}'
