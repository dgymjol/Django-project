from django.db import models

class Users(models.Model):
    user_id = models.CharField(max_length=255)
    user_pw = models.CharField(max_length=255)
    user_email = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    
    def __str__(self):
        return f"id: {self.user_id} | name: {self.user_name}"
    
class SaveVideos(models.Model):
    user_id = models.CharField(max_length=255)
    video_id = models.IntegerField()
    def __str__(self):
        return f"user_id: {self.user_id} | video_id: {self.video_id}"
      
class VideoList(models.Model):
    video_category = models.CharField(max_length=255)
    video_url = models.CharField(max_length=511)
    video_name = models.CharField(max_length=255)
    def __str__(self):
        return f"id: {self.id} | name: {self.video_name} | category: {self.video_category}"
  