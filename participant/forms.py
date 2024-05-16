from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']

    # Specify URLField with required=False for optional URLs
    website_link = forms.URLField(required=False)
    facebook = forms.URLField(required=False)
    twitter = forms.URLField(required=False)
    pinterest = forms.URLField(required=False)
    dribbble = forms.URLField(required=False)
    behance = forms.URLField(required=False)