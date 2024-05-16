from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ['user']
        widgets = {
            'certificate_image': forms.FileInput(attrs={'accept': 'image/*'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].required = False


from django import forms
from .models import Response

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['answer']


