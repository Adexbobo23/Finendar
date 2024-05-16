from django.conf import settings
from django.db import models

class Course(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    free_regular_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=255, default='2 hours')
    lesson_set = models.CharField(max_length=255, default='30 lessons')
    about_course = models.TextField()
    start_date = models.DateField()
    language = models.CharField(max_length=100)
    requirements = models.TextField()
    description = models.TextField()
    course_tags = models.TextField()
    video_url = models.URLField()
    certificate_image = models.ImageField(upload_to='certificate_templates/', blank=True, null=True)
    course_image = models.ImageField(upload_to='course_images/', blank=True, null=True)
    
    # Fields for course lessons
    lesson_1 = models.URLField(blank=True, null=True)
    lesson_2 = models.URLField(blank=True, null=True)
    lesson_3 = models.URLField(blank=True, null=True)
    lesson_4 = models.URLField(blank=True, null=True)
    lesson_5 = models.URLField(blank=True, null=True)
    lesson_6 = models.URLField(blank=True, null=True)
    lesson_7 = models.URLField(blank=True, null=True)
    lesson_8 = models.URLField(blank=True, null=True)
    lesson_9 = models.URLField(blank=True, null=True)
    lesson_10 = models.URLField(blank=True, null=True)
    lesson_11 = models.URLField(blank=True, null=True)
    lesson_12 = models.URLField(blank=True, null=True)
    lesson_13 = models.URLField(blank=True, null=True)
    lesson_14 = models.URLField(blank=True, null=True)
    lesson_15 = models.URLField(blank=True, null=True)
    lesson_16 = models.URLField(blank=True, null=True)
    lesson_17 = models.URLField(blank=True, null=True)
    lesson_18 = models.URLField(blank=True, null=True)
    lesson_19 = models.URLField(blank=True, null=True)
    lesson_20 = models.URLField(blank=True, null=True)
    lesson_21 = models.URLField(blank=True, null=True)
    lesson_22 = models.URLField(blank=True, null=True)
    lesson_23 = models.URLField(blank=True, null=True)
    lesson_24 = models.URLField(blank=True, null=True)
    lesson_25 = models.URLField(blank=True, null=True)
    lesson_26 = models.URLField(blank=True, null=True)
    lesson_27 = models.URLField(blank=True, null=True)
    lesson_28 = models.URLField(blank=True, null=True)
    lesson_29 = models.URLField(blank=True, null=True)
    lesson_30 = models.URLField(blank=True, null=True)

    # Fields for course materials
    course_material_1 = models.FileField(upload_to='course_materials/', blank=True, null=True)
    course_material_2 = models.FileField(upload_to='course_materials/', blank=True, null=True)
    course_material_3 = models.FileField(upload_to='course_materials/', blank=True, null=True)
    course_material_4 = models.FileField(upload_to='course_materials/', blank=True, null=True)
    course_material_5 = models.FileField(upload_to='course_materials/', blank=True, null=True)


    def __str__(self):
        return self.title

# Cart ITEM
class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.course.title}'

    def total_price(self):
        return self.quantity * self.course.discounted_price


# models.py
from django.db import models
from django.conf import settings

class Question(models.Model):
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='questions')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='question_images/', blank=True, null=True)
    csv_file = models.FileField(upload_to='csv_files/', default=True)
    description = models.TextField(blank=True)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

class Response(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)


class ExamScore(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"Score: {self.score} by {self.user.username}"