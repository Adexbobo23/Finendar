from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'slug', 'free_regular_price', 'discounted_price', 'about_course', 
                  'start_date', 'language', 'requirements', 'description', 'course_tags', 
                  'video_url', 'certificate_image']
        widgets = {
            'certificate_image': forms.FileInput(attrs={'accept': 'image/*'}),  # Optional: Add file input widget
        }

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['certificate_image'].required = False  # Make certificate_image field optional
