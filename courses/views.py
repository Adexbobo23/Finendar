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

class UploadQuestionsView(View):
    template_name = 'upload_questions.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        csv_file = request.FILES.get('file')
        if csv_file is not None:
            df = pd.read_csv(csv_file)
            for _, row in df.iterrows():
                question_text = row.get('question_text')  # Get the question text
                correct_option = row.get('correct_option')  # Get the correct option
                if question_text and correct_option:  # Check if question text and correct option are not None
                    # Create the Question object
                    question = Question.objects.create(text=question_text)
                    # Create the Answer object with the correct option
                    answer = Answer.objects.create(question=question, text=correct_option)
            return redirect('home')
        return render(request, self.template_name)


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
