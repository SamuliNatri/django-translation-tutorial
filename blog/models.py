from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, blank=False, default='')
    body = models.TextField(blank=False, default='')
    slug = models.SlugField(max_length=255, blank=False, unique=True)

    def __str__(self):
        return self.title
