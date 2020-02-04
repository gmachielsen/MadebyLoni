from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=250, unique=True)
	slug = models.SlugField(max_length=250, unique=True)
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to='category', blank=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def get_url(self):
		return reverse('shop:products_by_category', args=[self.slug])

	def __str__(self):
		return '{}'.format(self.name)



class Product(models.Model):
	SIZES = (
		('X', 'No size selected'),
		('4', 'Size 4'),
		('6', 'Size 6'),
		('8', 'Size 8'),
		('10','Size 10'),
		('12', 'Size 12'),
		('14', 'Size 14'),
		('16', 'Size 16'),
	)

	TYPES = (
		('X', 'Select type'),
		('D', 'Dresses'),
		('B', 'Bracelets')
	)

	COLOURS = (
		('X', 'Select colour'),
		('Black', 'Black'),
		('White', 'White'),
		('Red', 'Red'),
		('Orange', 'Orange'),
		('Yellow', 'Yellow'),
		('Green', 'Green'),
		('Blue', 'Blue'),
		('Purple', 'Purple'),
		('Pink', 'Pink'),
		('Brown', 'Brown'),
		('Different', 'Different'),
	)
	name = models.CharField(max_length=250, unique=True)
	slug = models.SlugField(max_length=250, unique=True)
	description = models.TextField(blank=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	image = models.ImageField(upload_to='product', blank=True)
	size = models.CharField(blank=True, null=True, max_length=1, default='X', choices=SIZES)
	type = models.CharField(blank=True, null=True, max_length=1, default='X', choices=TYPES)
	color = models.CharField(blank=True, null=True, max_length=1, default='X', choices=COLOURS)
	stock = models.IntegerField()
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	views = models.IntegerField(default=0)

	class Meta:
		ordering = ('name',)
		verbose_name = 'product'
		verbose_name_plural = 'products'

	def get_url(self):
		return reverse('shop:ProdCatDetail', args=[self.category.slug, self.slug])

	def __str__(self):
		return '{}'.format(self.name)

class ProductImages(models.Model):
    productpictures = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
    images = models.ImageField(upload_to='product_images', blank=True)
