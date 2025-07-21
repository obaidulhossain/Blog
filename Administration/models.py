from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class SiteSettings(models.Model):
    pass


class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sidebar_expanded = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.user.username}'s Settings"