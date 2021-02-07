from rest_framework import serializers

from core.models import *


class TheaterSerializer(models.Model):
    pass


class HallSerializer(serializers.ModelSerializer):
    pass


class MovieSerializer(serializers.ModelSerializer):
    pass


class ScreeningSerializer(models.Model):
    pass


class TicketSerializer(models.Model):
    pass
