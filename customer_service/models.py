from django.db import models
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=250, blank=False)
    email = models.EmailField(max_length=250, blank=False)
    phone = models.CharField(max_length=250, blank=False)
    message = models.TextField(blank=False)

    def __str__(self):
        return '{}'.format(self.name)
