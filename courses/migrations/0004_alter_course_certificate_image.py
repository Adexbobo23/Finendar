# Generated by Django 5.0.1 on 2024-02-12 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_remove_coursebuildertopic_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='certificate_image',
            field=models.ImageField(blank=True, null=True, upload_to='certificate_templates/'),
        ),
    ]