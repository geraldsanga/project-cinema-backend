from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
from .models import Category, Hall, Movie, Theater, Ticket, Screening, Seat


@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ('theater', 'name')


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    pass

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    pass


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'premier_date')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["duration"].label = "Duration(hrs) eg: 2.30 for 2 hours and a half"
        return form


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Screening)
class ScreeningAdmin(admin.ModelAdmin):
    pass


@admin.register(Theater)
class TheaterAdmin(LeafletGeoAdmin):
    list_display = ('name', 'contact_number')
    fields = ('name', 'image', 'contact_number', 'location')
    search_fields = ['name']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["location"].label = "Location on the map"
        return form
