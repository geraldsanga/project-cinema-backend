from django.utils.html import mark_safe
from django.contrib.auth.models import User
from django.contrib.gis.db import models as  gis_models
from django.db import models


class Theater(models.Model):
    name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=14)
    image = models.ImageField(upload_to='theater_images/')
    location = gis_models.PointField(srid=4326, geography=True)

    def __str__(self):
        return self.name


class Hall(models.Model):
    name = models.CharField(max_length=50)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.theater}'

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name} - Genre'
    class Meta:
        verbose_name = 'Movie Category'
        verbose_name_plural = 'Movie Categories'

class Movie(models.Model):
    duration = models.IntegerField()
    description = models.TextField()
    premier_date = models.DateField()
    title = models.CharField(max_length=30)
    director = models.CharField(max_length=30)
    image = models.ImageField(upload_to='movie_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.title}'


class Screening(models.Model):
    start_time = models.DateTimeField()
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.movie} at {self.start_time}'




class Ticket(models.Model):
    price = models.IntegerField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    screening = models.ForeignKey(Screening, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.customer}\'s ticket for {self.screening}'

class Seat(models.Model):
    row = models.CharField(max_length=1)
    number = models.CharField(max_length=2)
    price = models.IntegerField(blank=True, null=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    screening = models.ForeignKey(Screening, on_delete=models.CASCADE)

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