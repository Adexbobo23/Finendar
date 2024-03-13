from django.shortcuts import render, redirect, get_object_or_404
from .forms import CourseForm
from .models import Course
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def create_project(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course_instance = form.save(commit=False)
            course_instance.user = request.user 
            course_instance.save()
            return redirect('instructors_dashboard')
    else:
        form = CourseForm()
    
    return render(request, 'dashboard/create-course.html', {'form': form})


def all_courses(request):
    courses = Course.objects.all()
    return render(request, 'course.html', {'courses': courses})


def course_details(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    # Fetch the latest 2 courses
    courses = Course.objects.order_by('-id')[:2]
    context = {
        'course': course,
        'courses': courses
    }
    return render(request, 'course-details.html', context)


def wbt(request):
    return render(request, 'cbt.html')

# ==========================================WEB BASE TEST=============================================

import pandas as pd
from django.shortcuts import render, redirect
from django.views import View
from .models import Question, Answer, Response
from .forms import ResponseForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def upload_questions(request):
    if request.method == 'POST':
        csv_file = request.FILES.get('csv_file')
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        if csv_file and title:
            question = Question.objects.create(
                title=title,
                description=description,
                image=image,
                csv_file=csv_file
            )
            question.users.add(request.user)
            return redirect('question_success')

    return render(request, 'upload_questions.html')


@login_required(login_url='login')
def question_upload(request):
    return render(request, 'question-upload-success.html')


def question_list(request):
    questions = Question.objects.all()
    return render(request, 'wbt-grid.html', {'questions': questions})

# @login_required(login_url='login')
# def upload_questions(request):
#     if request.method == 'POST':
#         csv_file = request.FILES.get('file')
#         if csv_file is not None:
#             # Get the currently logged-in user
#             instructor = request.user
#             df = pd.read_csv(csv_file)
#             for _, row in df.iterrows():
#                 question_text = row.get('question_text')  # Get the question text
#                 options = [row.get('option1'), row.get('option2'), row.get('option3'), row.get('option4')]  # Get all options
#                 correct_option = row.get('correct_option')  # Get the correct option
#                 if question_text and all(options) and correct_option:  # Check if all required fields are not None
#                     # Create the Question object and assign it to the instructor
#                     question = Question.objects.create(text=question_text)
#                     question.users.add(instructor)
#                     # Create Answer objects for all options and mark the correct option
#                     for option_text in options:
#                         answer = Answer.objects.create(question=question, text=option_text)
#                         if option_text == correct_option:
#                             question.correct_answer = answer
#                             question.save()
#             return redirect('home')
#     return render(request, 'upload_questions.html')


class TakeExamView(View):
    template_name = 'cbt.html'

    def get(self, request):
        questions = Question.objects.all()
        form = ResponseForm()
        return render(request, self.template_name, {'questions': questions, 'form': form})

    def post(self, request):
        form = ResponseForm(request.POST)
        if form.is_valid():
            user = request.user
            question_id = request.POST.get('question')
            selected_option = request.POST.get('selected_option')

            question = get_object_or_404(Question, pk=question_id)
            correct_option = question.answer_set.first().text

            if selected_option == correct_option:
                # Increment user's score or do any other required actions
                pass

            # Save the response
            response = form.save(commit=False)
            response.user = user
            response.question = question
            response.selected_option = selected_option
            response.save()

            return redirect('exam_result')

        return render(request, self.template_name, {'form': form})


def exam_result(request):
    # Implement scoring logic here
    return render(request, 'exam_result.html')
