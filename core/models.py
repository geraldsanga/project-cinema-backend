from django.utils.html import mark_safe
from django.contrib.auth.models import User
from django.contrib.gis.db import models as  gis_models
from django.db import models


class Theater(models.Model):
    name = models.CharField(max_length=50)
    location = gis_models.PointField(srid=4326, geography=True)
    contact_number = models.CharField(max_length=14)

    def __str__(self):
        return self.name


class Hall(models.Model):
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} - {self.theater}'


class Movie(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='movie_images/')
    premier_date = models.DateField()
    duration = models.IntegerField()
    description = models.TextField()


    def __str__(self):
        return f'{self.title}'


class Screening(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    start_time = models.DateTimeField()

    def save(self, *args, **kwargs):
        if self.start_time > self.movie.final_date or self.start_time < self.movie.premier_date:
            raise ValueError('The date is not as per the time range the movie will be shown')
        super(Screening, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.movie} show in {self.hall.theater} - {self.hall} at {self.start_time}'


class Seat(models.Model):
    row = models.CharField(max_length=1)
    number = models.CharField(max_length=2)
    price = models.IntegerField(blank=True, null=True)

    def calculate_seat_price(self, row):
        if row == 'A' or 'B' or 'C' or 'D' or 'E':
            return 7500
        else:
            return 1000

    def save(self, *args, **kwargs):
        self.price = self.calculate_seat_price(self.row)
        super(Seat, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.row}{self.number}'


class Ticket(models.Model):
    screening = models.ForeignKey(Screening, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    seat = models.ManyToManyField(Seat)
    time_created = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.customer}\'s ticket for {self.screening}'
