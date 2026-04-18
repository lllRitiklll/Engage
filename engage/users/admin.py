from django.contrib import admin
from .models import User, Follow, Notification

admin.site.register(User)
admin.site.register(Follow)
admin.site.register(Notification)