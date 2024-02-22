from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey('Category', null=True, on_delete=models.CASCADE, )
    photo = models.ForeignKey('Image', null=True, on_delete=models.CASCADE, )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Image(models.Model):
    active = models.BooleanField(default=True)
    postID = models.ForeignKey('Post', null=True, on_delete=models.CASCADE, )
    image = models.FileField(null=True)
    title = models.CharField(max_length=120)

    def __unicode__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()

    def __str__(self):
        return self.name
