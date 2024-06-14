from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Customer


class CustomUserAdmin(UserAdmin):
    pass

class CustomerAdmin(admin.ModelAdmin):
    pass

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Customer, CustomerAdmin)