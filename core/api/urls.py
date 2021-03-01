from django.urls import path

from .views import (NowPlayingMovies, OpeningThisWeekMovies, CategoryView,
                    AllTheaters, NearByTheaters, MovieScreenings, BookATicketView)

urlpatterns = [
    path('book_a_ticket/<str:row>/<int:number>/', BookATicketView.as_view(), name='book_a_ticket'),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('movie_screenings/<int:pk>', MovieScreenings.as_view(), name='movie_screenings'),
    path('nearby_theaters/', NearByTheaters.as_view(), name='nearby_theaters'),
    path('now_playing_movies/', NowPlayingMovies.as_view(), name='now_playing_movies'),
    path('opening_this_week_movies/', OpeningThisWeekMovies.as_view(), name='opening_this_week_movies'),
    path('theaters/', AllTheaters.as_view(), name='theaters'),
]