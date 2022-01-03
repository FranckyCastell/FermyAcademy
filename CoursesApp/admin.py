from django.contrib import admin
from CoursesApp.models import Courses

# Register your models here.


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name']  # COL DATA
    search_fields = ['name']  # SEARCH DATA


class CoursesAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']  # READ FIELDS
    list_display = ['title', 'price', 'updated']  # COL DATA
    search_fields = ['title']  # SEARCH DATA


admin.site.register(Courses, CoursesAdmin)
