from django.contrib import admin
from .models import Course, Question, Answer, Response, ExamScore

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'language', 'user')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('display_users', 'title', 'csv_file', 'description')

    def display_users(self, obj):
        return ", ".join([user.username for user in obj.users.all()])
    display_users.short_description = 'Users'

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'text')

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'answer')

@admin.register(ExamScore)
class ExamScoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'score')
