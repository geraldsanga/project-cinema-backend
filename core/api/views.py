from datetime import datetime, timedelta

from rest_framework import status, views
from rest_framework.response import Response


from core.models import Movie
from core.api.serializers import MovieSerializer


class NowPlayingMovies(views.APIView):
    """
    This view will return all the movies that are currently been shown,
    that is: movies that are still within a 28 days range from the day
    they premiered.
    """
    now_playing_movies = list()

    def is_it_currently_playing(self, movie):
        today = datetime.today().date()
        movie_final_date = movie.premier_date + timedelta(days=30)
        if movie_final_date > today:
            return movie
        else:
            pass

    def get(self, request):

        movies = Movie.objects.all()
        for movie in movies:
            if self.is_it_currently_playing(movie) is not None:
                self.now_playing_movies.append(movie)
        serializer = MovieSerializer(self.now_playing_movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
