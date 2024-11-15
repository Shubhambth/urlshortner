# shortener/models.py
from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User


class ShortenedURL(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    original_url = models.URLField()
    short_path = models.CharField(max_length=6, unique=True, blank=True)
    visits = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.short_path:
            self.short_path = get_random_string(6)
        super().save(*args, **kwargs) 
