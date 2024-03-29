# Generated by Django 5.0.1 on 2024-02-03 06:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('display_name', models.CharField(max_length=50)),
                ('skill_occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('website_link', models.URLField(default='')),
                ('bio', models.TextField(blank=True, null=True)),
                ('facebook', models.URLField(default='')),
                ('twitter', models.URLField(default='')),
                ('linkedin', models.URLField(default='')),
                ('pinterest', models.URLField(default='')),
                ('dribbble', models.URLField(default='')),
                ('behance', models.URLField(default='')),
                ('github', models.URLField(default='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
