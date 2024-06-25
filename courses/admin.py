from django.contrib import admin
from .models import Course, Question, Answer, Response, ExamScore, CartItem, EnrolledCourse, Wishlist

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'language', 'user')


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'added_on')
    search_fields = ('user__username', 'course__title')
    list_filter = ('added_on',)
    date_hierarchy = 'added_on'
    ordering = ('-added_on',)

@admin.register(EnrolledCourse)
class EnrolledCourseAdmin(admin.ModelAdmin):
    list_display = ('course', 'user', 'enrolled_date')

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

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'quantity', 'added_at']