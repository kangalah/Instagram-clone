from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Post(models.Model):
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    caption = models.TextField()
    likes = models.ManyToManyField(User, related_name='likes', blank=True,)
    # user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.caption

class profile(models.Model):
    name = models.CharField(blank=True, max_length=120)
