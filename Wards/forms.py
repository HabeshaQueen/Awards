from django import forms
from .models import *

class UploadForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name','view','description','link') 


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user_id'] 

