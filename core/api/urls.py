from django.urls import path

from .views import NowPlayingMovies, OpeningThisWeekMovies

urlpatterns = [
    path('now_playing_movies/', NowPlayingMovies.as_view(), name='now_playing_movies'),
    path('opening_this_week_movies/', OpeningThisWeekMovies.as_view(), name='opening_this_week_movies'),

]