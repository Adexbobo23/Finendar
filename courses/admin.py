from django.contrib import admin
from .models import Course, Question, Answer, Response

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'language', 'user')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text',)

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'text')

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'answer')
