from django.contrib import admin
from .models import Category, Product, ProductImages

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    populated_fields = {'slug':('name',)}
admin.site.register(Category, CategoryAdmin)

class ProductImageInline(admin.TabularInline):
    model = ProductImages
    extra = 3

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
    inlines = [ ProductImageInline, ]




admin.site.register(Product, ProductAdmin)
