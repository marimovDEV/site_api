from django.contrib import admin
from .models import HomeVideo, Order,AdminProfile




class AdminProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_superadmin', 'phone_number')
    search_fields = ('user__username', 'user__email')

admin.site.register(AdminProfile, AdminProfileAdmin)

@admin.register(HomeVideo)
class HomeVideoAdmin(admin.ModelAdmin):
    list_display = ('video', 'is_active')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'created_at')


