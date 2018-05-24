from django.contrib import admin
from WOW.models import*

# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date', 'url')
admin.site.register(Item, ItemAdmin)

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
admin.site.register(UserInfo, UserInfoAdmin)
