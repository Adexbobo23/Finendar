from django import forms
from .models import Survey, Question

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['title', 'description']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['survey', 'question_type', 'question_text', 'choices']
        widgets = {
            'choices': forms.Textarea(attrs={'rows': 3, 'cols': 40}),  
        }


from django import forms
from .models import Answer, Response

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = []

    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions', None)
        super(ResponseForm, self).__init__(*args, **kwargs)
        for question in questions:
            if question.question_type == Question.TEXT:
                self.fields[f'question_{question.id}_text'] = forms.CharField(label=question.question_text, widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}), required=False)
            elif question.question_type == Question.MULTIPLE_CHOICE:
                choices = [(choice.strip(), choice.strip()) for choice in question.choices.split(',') if choice.strip()]
                self.fields[f'question_{question.id}_choice'] = forms.ChoiceField(label=question.question_text, choices=choices, widget=forms.RadioSelect(), required=False)
