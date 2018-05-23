from django.contrib import admin
from WOW.models import*

# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    pass
admin.site.register(Item, ItemAdmin)
