from django.urls import path

from .views import (NowPlayingMovies, OpeningThisWeekMovies, CategoryView,
                    AllTheaters, NearByTheaters, MovieScreenings)

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='categories'),
    path('now_playing_movies/', NowPlayingMovies.as_view(), name='now_playing_movies'),
    path('opening_this_week_movies/', OpeningThisWeekMovies.as_view(), name='opening_this_week_movies'),
    path('theaters/', AllTheaters.as_view(), name='theaters'),
    path('nearby_theaters/', NearByTheaters.as_view(), name='nearby_theaters'),
    path('movie_screenings/<int:id>', MovieScreenings.as_view(), name='movie_screenings')
]