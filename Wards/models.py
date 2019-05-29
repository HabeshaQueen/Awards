from django.shortcuts import render,redirect
from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Project(models.Model):

    name = models.CharField(max_length=50, blank=True)
    view = models.ImageField(upload_to = 'gallery/')
    description = models.TextField(max_length=500, blank=True)
    link = models.CharField(max_length=50, blank=True)
    date_posted = models.DateTimeField(auto_now=True)
    editor = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.description

    def save_image(self):
        self.save()

    def set_description(self,new_description):
        self.description = new_description
        self.save()

    @classmethod
    def search_by_name(cls,search_term):
        project = Project.objects.filter(name__icontains = search_term)
        return project

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profile/')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    contacts=models.CharField(max_length=50, blank=True)
    bio = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering=['-profile_photo']

    def __str__(self):
        return self.contacts

    def save_user(self):
        self.save()

    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user_id=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Vote(models.Model):
    design=models.IntegerField(default=0,validators=[MaxValueValidator(20)])
    usability=models.IntegerField(default=0,validators=[MaxValueValidator(20)])
    content=models.IntegerField(default=0,validators=[MaxValueValidator(20)])
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    project=models.IntegerField(default=0)

      