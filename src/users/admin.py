from django.contrib import admin

from .models import User, Role, Profile

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ("last_login", "date_joined")

@admin.register(Profile)
class ProfileAdminn(admin.ModelAdmin):
    pass

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass

