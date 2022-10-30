from django.db import models
from user.models import User


class Post(models.Model):
    title = models.CharField("Post title",  max_length=250, null=True, blank=True)
    description = models.TextField('Post description', null=True, blank=True)
    image = models.ImageField('Post image', null=True, blank=True)
    slug = models.SlugField('Unique slug id', max_length=50, unique=True)
    creation_date = models.DateTimeField('Publish date', auto_now_add=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="posts")


class Like(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="likes")
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE, related_name="likes")
    is_liked = models.BooleanField(default=False)
    creation_date = models.DateTimeField('Publish date', auto_now_add=True)

# Create your models here.
