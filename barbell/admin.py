from django.contrib import admin
from .models import User, Welcome, Info

@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = [
    'id', 'name', 'email', 'is_committee', 'is_member', 'image'
    ]