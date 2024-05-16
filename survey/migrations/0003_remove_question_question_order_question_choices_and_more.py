# Generated by Django 5.0.4 on 2024-04-08 14:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_question_question_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_order',
        ),
        migrations.AddField(
            model_name='question',
            name='choices',
            field=models.TextField(blank=True, help_text='Comma-separated choices for multiple-choice questions', null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('text', 'Text'), ('multiple_choice', 'Multiple Choice')], default='text', max_length=20),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_answer', models.TextField(blank=True, null=True)),
                ('choice_answer', models.CharField(blank=True, max_length=255, null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.question')),
                ('response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='survey.response')),
            ],
        ),
    ]