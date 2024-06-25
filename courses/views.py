from django.shortcuts import render, redirect, get_object_or_404
from .forms import CourseForm
from .models import Course, CartItem, EnrolledCourse, Wishlist
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages


@login_required(login_url='login')
def create_project(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course_instance = form.save(commit=False)
            course_instance.user = request.user
            course_instance.save()
            return redirect('instructors_dashboard')
        else:
            print(form.errors) 
    else:
        form = CourseForm()

    return render(request, 'dashboard/create-course.html', {'form': form})


@login_required(login_url='login')
def add_to_wishlist(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user, course=course)
    
    if created:
        messages.success(request, f'Course "{course.title}" has been added to your wishlist.')
    else:
        messages.info(request, f'Course "{course.title}" is already in your wishlist.')
    
    return redirect('all_courses')


@login_required(login_url='login')
def all_courses(request):
    query = request.GET.get('q')
    page = request.GET.get('page', 1)
    
    if query:
        courses = Course.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains(query)) |
            Q(course_tags__icontains(query))  
        )
    else:
        courses = Course.objects.all()
    
    paginator = Paginator(courses, 9)
    try:
        courses_paginated = paginator.page(page)
    except PageNotAnInteger:
        courses_paginated = paginator.page(1)
    except EmptyPage:
        courses_paginated = paginator.page(paginator.num_pages)
    
    user_wishlist = Wishlist.objects.filter(user=request.user).values_list('course_id', flat=True)
    
    return render(request, 'course.html', {
        'courses': courses_paginated,
        'query': query,
        'paginator': paginator,
        'user_wishlist': user_wishlist
    })


@login_required(login_url='login')
def toggle_wishlist(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, course=course)

    if not created:
        wishlist_item.delete()

    return redirect('course_details', course_id=course_id)


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
def enroll_user(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    # Check if the user is already enrolled
    if EnrolledCourse.objects.filter(user=request.user, course=course).exists():
        messages.warning(request, 'You are already enrolled in this course.')
    else:
        # Enroll the user in the course
        EnrolledCourse.objects.create(user=request.user, course=course)
        messages.success(request, 'You have been successfully enrolled in the course.')
    
    # Redirect to the "my-course" page after enrollment
    return redirect('my-course')


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

    if request.method == 'POST' and 'enroll_course' in request.POST:
        return enroll_user(request, course_id)  

    return render(request, 'course-details.html', context)


@login_required(login_url='login')
def course_lesson(request, course_id):
    enrolled_course = get_object_or_404(EnrolledCourse, course_id=course_id, user=request.user)
    course = enrolled_course.course
    lessons = [
        course.lesson_1, course.lesson_2, course.lesson_3, course.lesson_4, course.lesson_5,
        course.lesson_6, course.lesson_7, course.lesson_8, course.lesson_9, course.lesson_10,
        course.lesson_11, course.lesson_12, course.lesson_13, course.lesson_14, course.lesson_15,
        course.lesson_16, course.lesson_17, course.lesson_18, course.lesson_19, course.lesson_20,
        course.lesson_21, course.lesson_22, course.lesson_23, course.lesson_24, course.lesson_25,
        course.lesson_26, course.lesson_27, course.lesson_28, course.lesson_29, course.lesson_30,
    ]

    return render(request, 'lesson.html', {'enrolled_course': enrolled_course, 'lessons': lessons})


def course_lesson_2(request):
    return render(request, 'lesson-2.html')


# ==========================================WEB BASE TEST=============================================

import pandas as pd
from django.shortcuts import render, redirect
from django.views import View
from .models import Question, Answer, Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

def wbt(request):
    return render(request, 'cbt.html')

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
