from django.urls import path
from . import views

app_name = 'streamapp'

urlpatterns = [
    path('stream/', views.stream, name='stream'),
    path('video_feed', views.video_feed, name='video_feed'),
    
]

