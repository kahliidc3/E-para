from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('products:product_list_by_category', args=[self.slug])

class Product(models.Model):
    SKIN_TYPE_CHOICES = [
        ('all', 'All Skin Types'),
        ('oily', 'Oily Skin'),
        ('dry', 'Dry Skin'),
        ('combination', 'Combination Skin'),
        ('sensitive', 'Sensitive Skin'),
    ]
    
    CONCERN_CHOICES = [
        ('acne', 'Acne Treatment'),
        ('aging', 'Anti-Aging'),
        ('brightening', 'Brightening'),
        ('hydration', 'Hydration'),
        ('sun_protection', 'Sun Protection'),
    ]
    
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    skin_type = models.CharField(max_length=20, choices=SKIN_TYPE_CHOICES, default='all')
    skin_concern = models.CharField(max_length=20, choices=CONCERN_CHOICES)
    ingredients = models.TextField(blank=True)
    how_to_use = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    requires_prescription = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.slug])
