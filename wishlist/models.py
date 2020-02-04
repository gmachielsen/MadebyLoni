from django.db import models
from django.conf import settings
from shop.models import Product

# Create your models here.
class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)# here CASCADE is the behavior to adopt when the referenced object(because it is a foreign key) is deleted. it is not specific to django,this is an sql standard.
    wished_item = models.ForeignKey(Product,on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=250, unique=True, blank=True, null=True)
    # slug = models.CharField(max_length=30,null=True,blank=True)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.wished_item.name
