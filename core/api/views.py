from datetime import datetime, timedelta

from rest_framework import status, views
from rest_framework.response import Response

from core.models import Movie, Theater
from core.api.serializers import MovieSerializer, TheaterSerializer


class NowPlayingMovies(views.APIView):
    """
    This view will return all the movies that are currently been shown,
    that is: movies that are still within a 30 days range from the day
    they premiered.
    """
    @staticmethod
    def is_it_currently_playing(movie):
        today = datetime.today().date()
        movie_final_date = movie.premier_date + timedelta(days=30)
        if movie_final_date > today > movie.premier_date:
            return movie

    def get(self, request):
        now_playing_movies = list()
        movies = Movie.objects.all()
        for movie in movies:
            if self.is_it_currently_playing(movie) is not None:
                now_playing_movies.append(movie)
        serializer = MovieSerializer(now_playing_movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OpeningThisWeekMovies(views.APIView):
    """
    This view will return all the movies that are currently playing, meaning:
    movies whose starting date is greater that today but less than seven days
    after today
    """
    @staticmethod
    def is_it_opening_this_week(movie):
        today = datetime.today().date()
        seven_days_from_now = today + timedelta(days=6)
        if today < movie.premier_date < seven_days_from_now:
            return movie

    def get(self, request):
        opening_this_week_movies = list()
        movies = Movie.objects.all()
        for movie in movies:
            if self.is_it_opening_this_week(movie) is not None:
                opening_this_week_movies.append(movie)
        serializer = MovieSerializer(opening_this_week_movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AllTheaters(views.APIView):
    """
    List all the theaters that are know by the application
    """

    def get(self, request):
        theaters = Theater.objects.all()
        serializer = TheaterSerializer(theaters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NearByTheaters(views.APIView):
    """
    Find theaters that are close to the current user location
    """
    pass
