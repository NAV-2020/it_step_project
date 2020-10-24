from django.contrib import admin

from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ("last_login", "date_joined")

