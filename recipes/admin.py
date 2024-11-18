from django.contrib import admin

# Register your models here.
# recipes/admin.py
from django.contrib import admin
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    ordering = ['created_at']

admin.site.register(Recipe, RecipeAdmin)

