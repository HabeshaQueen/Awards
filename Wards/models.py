from django.shortcuts import render,redirect
from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.dispatch import receiver
from django.db.models.signals import post_save


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
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    contacts=models.CharField(max_length=50, blank=True)
    website=models.CharField(max_length=50, blank=True)
    bio = models.CharField(max_length=100, blank=True)

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

class Reviews(models.Model):

    RATING_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
    )
    juror = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE, related_name='reviews',null=True)
    design = models.IntegerField(choices=RATING_CHOICES,default=0)
    usability = models.IntegerField(choices=RATING_CHOICES,default=0)
    content = models.IntegerField(choices=RATING_CHOICES,default=0)
    comment = models.CharField(max_length=200,null=True)

    @classmethod
    def get_reviews(cls):
        reviews = Reviews.objects.all()
        return reviews