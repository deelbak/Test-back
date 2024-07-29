from django.contrib import admin
from .models import Menu, MenuItem

class MenuItemInLine(admin.StackedInline):
    model = MenuItem
    extra = 1

class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInLine]


admin.site.register(Menu)

# Register your models here.
