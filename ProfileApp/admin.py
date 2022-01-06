from django.contrib import admin
from ProfileApp.models import Profile

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'cursos']  # COL DATA
    search_fields = ['name']  # SEARCH DATA


admin.site.register(Profile, ProfileAdmin)
