from django.contrib import admin
from .models import Profile

# Register your models here.

from django.contrib.auth.models import User, Group


class ProfileInline(admin.StackedInline):
    model = Profile
    
    
    
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]
    # Only display the "username" field
    
#there is no implementation for group in the thing im following
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Profile)