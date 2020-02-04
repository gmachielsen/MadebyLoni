from django.db import models
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    image = models.ImageField(upload_to='blog', blank=True)
    text = models.TextField(max_length=10000, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.title)

def get_url(self):
    return reverse('blog:BlogDetail', args=[self.slug])
