from django.shortcuts import render, redirect
from .models import Survey, Question
from .forms import SurveyForm, QuestionForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def create_survey(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            survey = form.save(commit=False)
            survey.created_by = request.user  
            survey.save()
            return redirect('survey_detail', survey_id=survey.id)
    else:
        form = SurveyForm()
    return render(request, 'survey/create_survey.html', {'form': form})

@login_required(login_url='login')
def create_question(request, survey_id):
    survey = Survey.objects.get(id=survey_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.survey = survey
            question.save()
            return redirect('survey_detail', survey_id=survey.id)
    else:
        form = QuestionForm()
    return render(request, 'survey/create_question.html', {'form': form, 'survey': survey})

@login_required(login_url='login')
def survey_detail(request, survey_id):
    survey = Survey.objects.get(id=survey_id)
    questions = survey.questions.all()
    return render(request, 'survey/survey_detail.html', {'survey': survey, 'questions': questions})

@login_required(login_url='login')
def all_survey(request):
    survey = Survey.objects.get(id=survey_id)
    questions = survey.questions.all()
    return render(request, 'survey/survey_detail.html', {'survey': survey, 'questions': questions})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Survey, Question, Response, Answer
from .forms import ResponseForm

@login_required(login_url='login')
def survey_list(request):
    surveys = Survey.objects.all()
    return render(request, 'survey/survey_list.html', {'surveys': surveys})

@login_required(login_url='login')
def survey_question_detail(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id)
    questions = survey.questions.all()
    if request.method == 'POST':
        form = ResponseForm(request.POST, questions=questions)  
        if form.is_valid():
            response = form.save(commit=False)
            response.survey = survey
            response.respondent = request.user
            response.save()
            
            for question in questions:
                answer_text = form.cleaned_data.get(f'question_{question.id}_text', None)
                answer_choice = form.cleaned_data.get(f'question_{question.id}_choice', None)
                
                # Check if answer_text and answer_choice are not None before using them
                if answer_text is not None:
                    Answer.objects.create(response=response, question=question, text_answer=answer_text)
                if answer_choice is not None:
                    Answer.objects.create(response=response, question=question, choice_answer=answer_choice)
            
            return redirect('survey_list')
    else:
        form = ResponseForm(questions=questions)
    
    # Convert choices to list for each question
    for question in questions:
        if question.question_type == 'multiple_choice':
            question.choices = [choice.strip() for choice in question.choices.split(',') if choice.strip()]

    return render(request, 'survey/survey_question_detail.html', {'survey': survey, 'questions': questions, 'form': form})
