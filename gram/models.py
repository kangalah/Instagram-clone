from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
from django.urls import reverse





class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, default=None)
    caption = models.TextField()

    

    def has_related_object(self):
        has_profile = False
        try:
            has_profile = (self.profile is not None)
        except Profile.DoesNotExist:
            pass
        return has_profile and (self.post is not None)

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.caption

    def get_absolute_url(self):
        return reverse('insta:post_detail',kwargs={'pk': self.pk})

    def total_likes(self):
        return self.likes.count()

class Comment(models.Model):
    image = models.ForeignKey(Post,blank=True, on_delete=models.CASCADE,related_name='comment', default=None, null=True)
    comment_owner = models.ForeignKey(User, blank=True, default=None, null=True)
    comment= models.TextField(null=True, default=None)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_image_comments(cls, id):
        comments = Comment.objects.filter(image__pk=id)
        return comments

    def __str__(self):
        return str(self.comment)








