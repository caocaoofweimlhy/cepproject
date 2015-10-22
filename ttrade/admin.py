from django.contrib import admin
from .models import Request, Favor, Tag
from accounts.models import UserProfile

admin.site.register(Request)
admin.site.register(Favor)
admin.site.register(Tag)
admin.site.register(UserProfile)