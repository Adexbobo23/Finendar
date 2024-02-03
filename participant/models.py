from django.db import models
from django.contrib.auth import get_user_model

class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    display_name = models.CharField(max_length=50, default='display_name')
    skill_occupation = models.CharField(max_length=100, blank=True, null=True)
    website_link = models.URLField(default='')
    bio = models.TextField(blank=True, null=True)

    # Profile Image
    profile_image = models.ImageField(upload_to='participant_profile_images/', blank=True, null=True)

    # Social Links
    facebook = models.URLField(default='')
    twitter = models.URLField(default='')
    linkedin = models.URLField(default='')
    pinterest = models.URLField(default='')
    dribbble = models.URLField(default='')
    behance = models.URLField(default='')
    github = models.URLField(default='')

    def __str__(self):
        return f"{self.user.username} - {self.display_name}"