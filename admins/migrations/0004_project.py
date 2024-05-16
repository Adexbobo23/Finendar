# Generated by Django 5.0.1 on 2024-04-23 19:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0003_remove_companyprofile_email_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255)),
                ('project_code', models.CharField(max_length=20, unique=True)),
                ('project_description', models.TextField()),
                ('project_image', models.ImageField(blank=True, null=True, upload_to='project_images/')),
                ('video_link', models.URLField(blank=True, null=True)),
                ('audio_link', models.URLField(blank=True, null=True)),
                ('website_url', models.URLField(blank=True, null=True)),
                ('deadline_date', models.DateField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_projects', to=settings.AUTH_USER_MODEL)),
                ('participants', models.ManyToManyField(related_name='projects_participated', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
