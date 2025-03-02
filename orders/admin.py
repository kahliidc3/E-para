from django.contrib import admin
from .models import Order, OrderItem, Prescription

# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'status', 'payment_method', 'payment_completed', 'created']
    list_filter = ['status', 'payment_method', 'payment_completed', 'created']
    search_fields = ['id', 'user__email']
    inlines = [OrderItemInline]
    raw_id_fields = ['user', 'address']
    date_hierarchy = 'created'
    ordering = ['-created']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'price', 'quantity']
    raw_id_fields = ['order', 'product']

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ['order_item', 'approved', 'created']
    list_filter = ['approved', 'created']
    readonly_fields = ['created']
