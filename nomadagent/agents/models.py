from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe


class TravelAgentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    keywords = models.TextField()
    profile = models.TextField()
    calendly_link = models.URLField()
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def img_preview(self): #new
        return mark_safe(f'<img src = "{self.image.url}" width = "300"/>')