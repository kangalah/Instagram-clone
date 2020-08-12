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
    likes = models.ManyToManyField(User, related_name='posts', blank=True)
    

    def has_related_object(self):
        has_profile = False
        try:
            has_profile = (self.profile is not None)
        except Profile.DoesNotExist:
            pass
        return has_profile and (self.car is not None)

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.caption

    def get_absolute_url(self):
        return reverse('insta:post_detail',kwargs={'id': self.id})

class Comment(models.Model):
    comment_owner = models.ForeignKey(User, blank=True, null=True, default=None)
    comment = models.TextField(null=True)

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

class Image(models.Model):
    pic=ImageField(manual_crop='1080x800', blank=True)
    name= models.CharField(max_length=55)
    caption = models.TextField(blank=True)
    profile= models.ForeignKey(User, blank=True,on_delete=models.CASCADE)
    



    def __str__(self):
        return str(self.name)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_profile_images(cls, profile):
        images = Image.objects.filter(profile__pk=profile)
        return images

class likes(models.Model):
    liker = models.ForeignKey(User)
    image =models.ForeignKey(Image)



