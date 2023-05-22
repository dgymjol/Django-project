from django.contrib import admin
from .models import Users, VideoList, SaveVideos

# Register your models here.
admin.site.register(Users)
admin.site.register(VideoList)
admin.site.register(SaveVideos)