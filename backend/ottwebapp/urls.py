from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('mypage/', views.mypage, name='mypage'),
    path('videos/<int:id>', views.play_video, name='videos'),
    path('testing/', views.testing, name='testing'),
]