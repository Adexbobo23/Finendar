# Generated by Django 5.0.4 on 2024-04-08 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]