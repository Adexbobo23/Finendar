# Generated by Django 5.0.1 on 2024-02-03 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0002_companyprofile_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='companyprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='companyprofile',
            name='last_name',
        ),
    ]
