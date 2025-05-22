from django.contrib import admin

# Register your models here.
from . models import Student
from . models import teacher
from . models import Homework
from . models import Answers


class studentadmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','email','pname','address','image','dob','password')

class teacheradmin(admin.ModelAdmin):
    list_display = ('name','subject','email','phonenumber','image','password')

class Homeworkadmin(admin.ModelAdmin):
    list_display = ('teachername','studentname','description','submissiondate')

class Answersadmin(admin.ModelAdmin):
    list_display = ('studentname','homework','answer_text','submitted_date')



admin.site.register(Student,studentadmin)
admin.site.register(teacher,teacheradmin)
admin.site.register(Homework,Homeworkadmin)
admin.site.register(Answers,Answersadmin)