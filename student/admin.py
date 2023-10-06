from django.contrib import admin
from student.models import *;

# Register your models here.
admin.site.site_header = "Horizon University admin login"
admin.site.site_title = "Horizon University Admin Portal"
admin.site.index_title = "Welcome to Horizon University Researcher Portal"  ;
admin.site.register(student)