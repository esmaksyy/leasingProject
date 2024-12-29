from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Device, CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('phone_number', 'first_name', 'last_name', 'email', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff')
    filter_horizontal = []
    search_fields = ('phone_number', 'first_name', 'last_name')
    ordering = ('phone_number',)
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
    )
    add_fieldsets = (
        (None, {'fields': ('phone_number', 'password1', 'password2')}),
    )


admin.site.register(Device)
admin.site.register(CustomUser, CustomUserAdmin)
