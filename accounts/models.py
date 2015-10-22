from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
import json

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    address = models.CharField(max_length=225, blank=True)
    age = models.IntegerField(default=1)
    karma = models.IntegerField(blank=True, default=0)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    contact = models.CharField(max_length=225, null=True, blank=True)
    timepoint = models.IntegerField(default=10)
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
        
    def get_absolute_url(self):
        return reverse("dashboard", kwargs={"pk":self.pk})

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])