from django.contrib import admin
from students.models import Student

#보여줄 컬럼 설정하기.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display =  ['s_name', 's_major']
