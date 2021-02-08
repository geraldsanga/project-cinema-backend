from django.urls import path

from .views import NowPlayingMovies

urlpatterns = [
    path('now_playing_movies/', NowPlayingMovies.as_view(), name='now_playing_movies')
]