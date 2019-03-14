from django.contrib import admin
from myapp.models import UserProfileInfo, User

# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserCreationForm

# Register your models here.

# class CustomUserAdmin(UserAdmin):
# 	add_form = CustomUserCreationForm
# 	model = CustomUser
# 	lis_display = ['email', 'username',]

admin.site.register(UserProfileInfo)
