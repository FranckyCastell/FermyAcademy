from django.contrib import admin
from AboutApp.models import Users

# Register your models here.


class UsersAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']  # COL DATA
    search_fields = ['name']  # SEARCH DATA
    list_filter = ['name']  # FILTER


admin.site.register(Users, UsersAdmin)
