from django.contrib import admin
from .models import Category, Product

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'skin_type', 'skin_concern', 'created', 'updated']
    list_filter = ['available', 'skin_type', 'skin_concern', 'created', 'updated', 'category']
    list_editable = ['price', 'stock', 'available', 'skin_type', 'skin_concern']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description', 'ingredients']
    date_hierarchy = 'created'
    ordering = ['name']
