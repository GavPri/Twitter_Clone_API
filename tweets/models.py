from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# Tweet/Post model
class Tweet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=300)
    image = models.ImageField(upload_to="images/", blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.id} {self.content[:20]}"
