from django.urls import path
from .views import homeView, detailView, videoView, partVideoView, moviehomeView

app_name = 'main_app'
urlpatterns = [
    path('', homeView, name='home'),
    path('movies', moviehomeView, name='home-movie'),
    path('episode/<slug:slug>', detailView, name='detail'),
    path('episode/video/<slug:slug>', videoView, name='video_file'),
    path('episode/part-video/<slug:slug>', partVideoView, name='part_video_file'),
]
