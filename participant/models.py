from django.db import models
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    current_job_place = models.CharField(max_length=255, default='')
    designation = models.CharField(max_length=255, default='')
    year_of_experience = models.CharField(max_length=10, default='')
    qualification = models.CharField(max_length=255, default='')
    email = models.EmailField(default='')
    phone_number = models.CharField(max_length=20, default='')
    website_link = models.URLField(default='')
    language = models.CharField(max_length=255, default='')
    career_objective = models.TextField(default='')

    # Social Links
    facebook = models.URLField(default='')
    twitter = models.URLField(default='')
    linkedin = models.URLField(default='')
    pinterest = models.URLField(default='')
    dribbble = models.URLField(default='')
    behance = models.URLField(default='')

    # Personal Information
    father_name = models.CharField(max_length=255, default='')
    mother_name = models.CharField(max_length=255, default='')
    national_id = models.CharField(max_length=20, default='')
    present_address = models.CharField(max_length=255, default='')
    permanent_address = models.CharField(max_length=255, default='')
    marital_status = models.CharField(max_length=20, default='')
    gender = models.CharField(max_length=20, default='')
    religion = models.CharField(max_length=255, default='')
    blood_group = models.CharField(max_length=5, default='')
    height = models.CharField(max_length=10, default='')
    weight = models.CharField(max_length=10, default='')

    # Education
    education_level = models.CharField(max_length=255, default='')
    major = models.CharField(max_length=255, default='')
    institute = models.CharField(max_length=255, default='')
    result_gpa = models.CharField(max_length=10, default='')
    starting_period_education = models.DateField(default='2000-01-01')  
    ending_period_education = models.DateField(default='2000-01-01')  

    # Employment
    company_name = models.CharField(max_length=255, default='')
    designation_employment = models.CharField(max_length=255, default='')
    starting_period_employment = models.DateField(default='2000-01-01')  
    ending_period_employment = models.DateField(default='2000-01-01')  
    responsibility = models.TextField(default='')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
