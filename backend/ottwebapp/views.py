from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Users, VideoList, SaveVideos


# mypage
def mypage(request):
    # TODO : user id hardcoding
    userid = 'dgymjol'
    
    user = Users.objects.filter(user_id=userid).values()[0]
    user_videos = SaveVideos.objects.filter(user_id=userid).values()
    all_videos = VideoList.objects.all().values()
    
    save_videos = []
    for user_video in user_videos:
        v_id = user_video['video_id']
        for video in all_videos:
            if v_id == video['id']:
                save_videos.append(video)

    template = loader.get_template('mypage.html')
    context = {
        'user' : user,
        'save_videos' : save_videos,
    }
    return HttpResponse(template.render(context, request))

def play_video(request, id):
    video = VideoList.objects.get(id=id)
    template = loader.get_template('play_video.html')
    context = {
        'v' : video,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    all_videos = VideoList.objects.all().values()
    template = loader.get_template('main.html')
    context = {
        'all_videos' : all_videos,
    }
    return HttpResponse(template.render(context, request))

def testing(request):
    users = Users.objects.all().order_by('user_name', '-id').values()
    videos = VideoList.objects.all().order_by('video_category', 'video_name').values()
    save_videos = SaveVideos.objects.all().order_by('user_id').values()
    
    # # SELECT * FROM members ORDER BY lastname ASC, id DESC;
    
    # specific_col = VideoList.objects.values_list('video_name')
    
    # specific_row = [
    #     VideoList.objects.filter(video_category='Music', id=1).values(),
    # #     # SELECT * FROM members WHERE video_category='Music' AND id = 1;
        
    # #     # Member.objects.filter(firstname='Emil').values() | Member.objects.filter(firstname='Tobias').values()
    # #     # SELECT * FROM members WHERE firstname = 'Emil' OR firstname = 'Tobias';

    # #     # SQL WHERE (https://www.w3schools.com/django/django_queryset_filter.php)
        
    #     ]
    
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry'], 
        'users' : users,
        'videos' : videos,
        'save_videos' : save_videos,
        # 'specific_col' : specific_col,
        # 'specific_row': specific_row,
    }
    return HttpResponse(template.render(context, request))