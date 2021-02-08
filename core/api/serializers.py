from rest_framework import serializers

from core.models import *


class TheaterSerializer(serializers.ModelSerializer):
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
