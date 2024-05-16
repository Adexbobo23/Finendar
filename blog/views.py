from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from participant.models import UserProfile
from .models import Blog
from .forms import BlogForm

@login_required(login_url='login')
def blog(request):
    user_profile = UserProfile.objects.get(user=request.user)
    blogs = Blog.objects.all()
    context = {'user_profile': user_profile, 'blogs': blogs}
    return render(request, 'blog.html', context)

@login_required(login_url='login')
def blog_details(request, blog_id):
    user_profile = UserProfile.objects.get(user=request.user)
    blog = get_object_or_404(Blog, pk=blog_id)
    blogs = Blog.objects.order_by('-created_at')[:5]
    context = {'user_profile': user_profile, 'blog': blog, 'blogs': blogs}
    return render(request, 'blog-details.html', context)


@login_required(login_url='login')
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog')
    else:
        form = BlogForm()

    user_profile = UserProfile.objects.get(user=request.user)
    context = {'user_profile': user_profile, 'form': form}
    return render(request, 'app/create-blog.html', context)