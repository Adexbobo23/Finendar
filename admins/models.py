from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

class Project(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_projects')
    project_name = models.CharField(max_length=255)
    project_code = models.CharField(max_length=20, unique=True)
    project_description = models.TextField()
    project_image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)
    audio_link = models.URLField(blank=True, null=True)
    website_url = models.URLField(blank=True, null=True)
    deadline_date = models.DateField()

    def __str__(self):
        return self.project_name

class ProjectParticipant(Project):
    participant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='project_participations')

    class Meta:
        verbose_name = 'Project Participant'
        verbose_name_plural = 'Project Participants'


class CompanyProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    display_name = models.CharField(max_length=50)
    skill_occupation = models.CharField(max_length=100, blank=True, null=True)
    website_link = models.URLField(default='')
    bio = models.TextField(blank=True, null=True)

    # Profile Image
    profile_image = models.ImageField(upload_to='company_profile_images/', blank=True, null=True)

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
