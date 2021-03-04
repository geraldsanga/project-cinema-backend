from datetime import datetime, timedelta
import pytz

from rest_framework import status, views
from rest_framework.response import Response

from django.contrib.auth.models import User
from core.models import Category, Movie, Theater, Ticket, Screening
from core.api.serializers import CategorySerializer, MovieSerializer, ScreeningSerializer, TheaterSerializer, TicketSerializer

hall_seats = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7',
              'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7']
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

class MovieScreenings(views.APIView):
    """
    Return all screenings for a particular movie that will show today
    """
    local_timezone = pytz.timezone('Africa/Dar_es_Salaam')

    def get(self, request, pk):
        today_screenings_for_movie = list()
        # 1. get the movie by it's id
        requested_movie = Movie.objects.get(id=pk)
        # 2. get all screenings for that movie
        current_time = datetime.now().replace(tzinfo=self.local_timezone)
        screening_today = datetime.today()
        # 3. filter the screenings to get those for today only
        # 4. see if the start time of the screening is greater than the time of the request
        for screening in Screening.objects.filter(movie=requested_movie):
            screening_start_time = screening.start_time.replace(tzinfo=self.local_timezone)
            if screening_start_time > current_time:
                today_screenings_for_movie.append(screening)
        # 5. Return those that satisfy all the conditions
        serializer = ScreeningSerializer(today_screenings_for_movie, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookATicketView(views.APIView):
    """
    Save a ticket for a customer, for a particular screening on a particular seat  in particular hall
    that matches the screening
    """
    def get(self, request, pk):
        screening = Screening.objects.get(id=pk)
        booked_tickets = Ticket.objects.filter(screening=screening)
        for ticket in booked_tickets:
            if ticket.seat in hall_seats:
                hall_seats.remove(ticket.seat)
        return Response(hall_seats, status=status.HTTP_200_OK)

    def post(self, request, screening_id, seat):
        customer = request.user
        screening = Screening.objects.get(id=screening_id)
        booked_seats = Ticket.objects.filter(screening=screening).values_list('seat', flat=True)
        print(booked_seats)
        if seat in booked_seats:
           return Response({"aborted": "NO"},status=status.HTTP_200_OK)
        else:
            Ticket.objects.create(customer=customer, screening=screening, seat=seat)
            return Response({"created": "OK"},status=status.HTTP_200_OK)      
        
        
class CategoryView(views.APIView):
    """Return all movie categories"""
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)