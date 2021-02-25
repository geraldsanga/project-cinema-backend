from rest_framework_gis import serializers as gis_serializers
from rest_framework import serializers
from core.models import *


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']


class TheaterSerializer(serializers.ModelSerializer):
    location = gis_serializers.GeometryField()

    class Meta:
        model = Theater
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = Movie
        fields = '__all__'


class ScreeningSerializer(serializers.ModelSerializer):
    movie_name = serializers.SlugRelatedField(read_only=True, slug_field='movie')
    hall = serializers.SlugRelatedField(read_only=True, slug_field='name')
    theater = serializers.SlugRelatedField(read_only=True, slug_field='name')
    start_time = serializers.DateTimeField(format="%d-%m-%Y %H %M")

    class Meta:
        model = Screening
        fields = ('movie_name', 'hall', 'theater', 'start_time')


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
