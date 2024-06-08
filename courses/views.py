from django.shortcuts import render, redirect, get_object_or_404
from .forms import CourseForm
from .models import Course, CartItem
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


@login_required(login_url='login')
def add_to_cart(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        course=course,
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('course_details', course_id=course_id)


@login_required(login_url='login')
def course_details(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    courses = Course.objects.order_by('-id')[:2]
    
    # Fetch cart items from the database
    cart_items = CartItem.objects.filter(user=request.user)

    context = {
        'course': course,
        'courses': courses,
        'cart_items': cart_items,
    }
    return render(request, 'course-details.html', context)



def wbt(request):
    return render(request, 'cbt.html')

# ==========================================WEB BASE TEST=============================================

import pandas as pd
from django.shortcuts import render, redirect
from django.views import View
from .models import Question, Answer, Response
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

@login_required(login_url='login')
def question_list(request):
    questions = Question.objects.all()
    return render(request, 'wbt-grid.html', {'questions': questions})


import pandas as pd
from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, ExamScore
import random

@login_required(login_url='login')
def take_exam(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    if request.method == 'POST':
        selected_option = request.POST.get('selected_option')
        correct_option = request.POST.get('correct_option')
        
        if selected_option == correct_option:
            # Increment user's score
            request.session.setdefault('score', 0)
            request.session['score'] += 1

        return redirect('exam_result')

    else:  # GET request
        csv_file_path = question.csv_file.path
        questions_df = pd.read_csv(csv_file_path)

        questions = []
        for index, row in questions_df.iterrows():
            question_text = row['question_text']
            options = [row['option1'], row['option2'], row['option3'], row['option4']]
            correct_option = row['correct_option']
            random.shuffle(options)
            questions.append({'question_text': question_text, 'options': options, 'correct_option': correct_option})

    return render(request, 'cbt.html', {'question': question, 'questions': questions})


@login_required(login_url='login')
def exam_result(request):
    # Retrieve the user's score from the session
    score = request.session.pop('score', 0)
    
    # Save the score to the database
    if request.user.is_authenticated:
        exam_score = ExamScore.objects.create(user=request.user, score=score)
    
    # You can implement further logic here if needed
    
    return render(request, 'exam_result.html', {'score': score})
