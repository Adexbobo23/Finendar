from django.db import models
from django.conf import settings

class Survey(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    TEXT = 'text'
    MULTIPLE_CHOICE = 'multiple_choice'
    CHOICE_FIELD_TYPES = [
        (TEXT, 'Text'),
        (MULTIPLE_CHOICE, 'Multiple Choice'),
        # Add more question types as needed
    ]

    survey = models.ForeignKey(Survey, related_name='questions', on_delete=models.CASCADE)
    question_type = models.CharField(max_length=20, choices=CHOICE_FIELD_TYPES, default=TEXT)
    question_text = models.TextField()
    choices = models.TextField(blank=True, null=True, help_text='Comma-separated choices for multiple-choice questions')

    def __str__(self):
        return self.question_text

class Response(models.Model):
    survey = models.ForeignKey(Survey, related_name='responses', on_delete=models.CASCADE)
    respondent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='survey_responses')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Response for {self.survey.title} by {self.respondent.username}'

class Answer(models.Model):
    response = models.ForeignKey(Response, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text_answer = models.TextField(blank=True, null=True)
    choice_answer = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'Answer for {self.question.question_text} in response to {self.response.survey.title}'
