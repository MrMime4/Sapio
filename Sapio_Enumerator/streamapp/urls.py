from django.urls import path
from . import views

app_name = 'streamapp'

urlpatterns = [
<<<<<<< HEAD
=======
    path('', views.home, name='home'),
>>>>>>> b5c60cd24ebed6da9eb4490924ee053df955720c
    path('stream/', views.stream, name='stream'),
    path('video_feed', views.video_feed, name='video_feed'),
    
]

