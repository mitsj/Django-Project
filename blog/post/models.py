from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    comment = models.CharField(max_length=1024, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.pk}: {self.title}'
