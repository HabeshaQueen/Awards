from rest_framework import serializers
from .models import *

class profile(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('profile_photo', 'contacts', 'Project','bio')

class project(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'view', 'description', 'link','date_posted')

