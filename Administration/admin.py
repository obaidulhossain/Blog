from django.contrib import admin
from .models import *


# Register your models here.
class UserSettingAdmin(admin.ModelAdmin):
    list_display = ("user", "sidebar_expanded")

admin.site.register(UserSettings, UserSettingAdmin)