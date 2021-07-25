from django.contrib import admin
from .models import Course
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display=('id','name','teacher','credits','compulsory','typeofcourse','campus')
    list_display_links=('id','name')
    list_per_page=20

admin.site.register(Course,CourseAdmin)