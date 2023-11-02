from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255, blank=False, default='')
    body = models.TextField(blank=False, default='')
    slug = models.SlugField(max_length=255, blank=False, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.slug])
