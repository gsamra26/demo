from django.contrib import admin
from .models import Student, Test, MetaTest

# Register your models here.
admin.site.register(Student)
admin.site.register(Test)
admin.site.register(MetaTest)
