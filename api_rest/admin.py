from django.contrib import admin

# Register your models here.

from .models import User, UserTasks

admin.site.register(User)
admin.site.register(UserTasks)
