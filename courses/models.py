from django.conf import settings
from django.db import models

class Course(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    free_regular_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    about_course = models.TextField()
    start_date = models.DateField()
    language = models.CharField(max_length=100)
    requirements = models.TextField()
    description = models.TextField()
    course_tags = models.TextField()

    video_url = models.URLField()
    certificate_image = models.ImageField(upload_to='certificate_templates/', blank=True, null=True)

