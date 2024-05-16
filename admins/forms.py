from django import forms
from .models import CompanyProfile
from django import forms
from userauth.models import Participant 
from .models import Project

class ProjectForm(forms.ModelForm):
    class DateInput(forms.DateInput):
        input_type = 'date'

    deadline_date = forms.DateField(widget=DateInput)

    class Meta:
        model = Project
        exclude = ['creator', 'participants']



class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        exclude = ['user']

    # Specify URLField with required=False for optional URLs
    website_link = forms.URLField(required=False)
    facebook = forms.URLField(required=False)
    twitter = forms.URLField(required=False)
    pinterest = forms.URLField(required=False)
    dribbble = forms.URLField(required=False)
    behance = forms.URLField(required=False)
