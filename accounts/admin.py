from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from.models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model=CustomUser
    list_display=['username','email','is_staff','is_active']
    search_fields=('username','email')
    fieldsets=UserAdmin.fieldsets + (
        ('Extra Info',{'fields':('bio','profile_pic')})
    )
admin.site.register(CustomUser, CustomUserAdmin)

