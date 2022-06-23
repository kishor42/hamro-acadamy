

# Register your models here.
from django.contrib import admin
from .models import Company, Course
# Register your models here.
admin.site.register(Company)

@admin.register(Course)

class CourseAdmin(admin.ModelAdmin):
  list_display=('course_number','course_name','max_numb_students','instructors')
