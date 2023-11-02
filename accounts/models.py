from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Account(models.Model):
    owner = models.OneToOneFiled(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=true)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to = 'images/', default='../default_profile_picture_dcasmd'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"