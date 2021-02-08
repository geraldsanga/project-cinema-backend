from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
from .models import *


@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ('theater', 'name')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["duration"].label = "Duration(hrs) eg: 2.30 for 2 hours and a half"
        return form


@admin.register(Screening)
class ScreeningAdmin(admin.ModelAdmin):
    pass


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    pass


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    actions_on_top = False


@admin.register(Theater)
class TheaterAdmin(LeafletGeoAdmin):
    list_display = ('name', 'contact_number')
    fields = ('name', 'contact_number', 'location')
    search_fields = ['name']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["location"].label = "Location on the map"
        return form
