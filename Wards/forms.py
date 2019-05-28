from django import forms
from .models import *
from rest_framework import serializers


class UploadForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name','view','description','link') 


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user_id'] 

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        exclude=['user','project']





        