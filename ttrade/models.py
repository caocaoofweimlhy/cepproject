from django.db import models
from django.core.urlresolvers import reverse
from accounts.models import UserProfile
import json

class Request(models.Model):
    Day_Choices = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )
    user = models.ForeignKey(UserProfile, blank=True, null=True, related_name="request_user")
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time = models.TimeField()
    recur = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    day = models.CharField(max_length=9, choices=Day_Choices, blank=True)
    other = models.TextField(blank=True)
    tag = models.ManyToManyField('Tag', related_name='requests', null=True, blank=True)
    acceptor = models.ForeignKey(UserProfile, blank=True, null=True, related_name="request_acceptor")
    accepted = models.BooleanField(default=False)
    duration = models.IntegerField(default=0, null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse("detailr", kwargs={"pk":self.pk})
    
    def __unicode__(self):
        return self.title

class Favor(models.Model):
    user = models.ForeignKey(UserProfile, blank=True, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("detailf", kwargs={"pk":self.pk})
    
class Tag(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title