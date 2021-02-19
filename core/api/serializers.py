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


class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = Movie
        fields = '__all__'


class ScreeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screening
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
