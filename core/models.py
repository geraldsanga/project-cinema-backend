from django.contrib.auth.models import User
from django.db import models


class Theater(models.Model):
    name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=14)

    def __str__(self):
        return self.name


class Hall(models.Model):
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    number_of_seats = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.theater}'


class Movie(models.Model):
    title = models.CharField(max_length=30)
    premier_date = models.DateField()
    final_date = models.DateField()
    duration = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f'{self.title}'


class Screening(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    start_time = models.DateTimeField()

    def __str__(self):
        return f'{self.movie} show in {self.hall.theater} - {self.hall} at {self.start_time}'


class Ticket(models.Model):
    screening = models.ForeignKey(Screening, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    seat = models.CharField(max_length=3)
    time_created = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.customer}\'s ticket for {self.screening}'
