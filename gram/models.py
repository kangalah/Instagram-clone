from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    caption = models.TextField()
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.caption


