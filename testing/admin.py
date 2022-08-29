from django.contrib import admin

# Register your models here.
from django.contrib import admin

from testing.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
  model = Profile
