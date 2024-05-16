from django.contrib import admin
from .models import CompanyProfile, Project, ProjectParticipant

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'project_code', 'deadline_date')

@admin.register(ProjectParticipant)
class ProjectParticipantAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'participant')
    
admin.site.register(CompanyProfile)
