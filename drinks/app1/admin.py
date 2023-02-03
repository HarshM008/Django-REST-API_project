from django.contrib import admin
from .models import drinks

@admin.register(drinks)
class drinksadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
