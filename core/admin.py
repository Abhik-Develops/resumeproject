from django.contrib import admin
from .models import FeedBack

# Register your models here.

@admin.register(FeedBack)

class UserAdmin(admin.ModelAdmin):
    
    list_display = ['id', 'name', 'email']
    ordering= ['id']