from django.contrib import admin

from menu.models import Menu, MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("__str__", "parent", "path")
    prepopulated_fields = {"path": ("name",)}


admin.site.register(Menu)
