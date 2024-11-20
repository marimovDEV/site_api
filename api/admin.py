from django.contrib import admin
from .models import HomeVideo, Order,AdminProfile,Product,Category
# from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group, User



admin.site.unregister(Group)
admin.site.unregister(User)
# admin.site.unregister(Token)


class AdminProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_superadmin', 'phone_number')
    search_fields = ('user__username', 'user__email')

admin.site.register(AdminProfile, AdminProfileAdmin)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category','name' )
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','description' )
@admin.register(HomeVideo)
class HomeVideoAdmin(admin.ModelAdmin):
    list_display = ('video', 'is_active')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'created_at')


