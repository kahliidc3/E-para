from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Address

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'phone_number', 'is_staff')
    search_fields = ('email', 'username', 'phone_number')
    ordering = ('email',)
    
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('phone_number', 'address')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('phone_number', 'address')}),
    )

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'street_address', 'city', 'state', 'postal_code', 'is_default')
    list_filter = ('city', 'state', 'is_default')
    search_fields = ('street_address', 'city', 'state', 'postal_code')
    raw_id_fields = ('user',)
