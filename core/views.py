from django.http import HttpResponse
from django.shortcuts import render
from .models import Seat


def add_seats(request):
    for _ in range(7):
        Seat.objects.create(row='B', number=(_+1))
    return HttpResponse()
