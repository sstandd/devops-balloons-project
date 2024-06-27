from django.contrib import admin
from .models import Flight, Balloon, Pilot, Airline, AirlinePilots


# Register your models here.

class FlightAdmin(admin.ModelAdmin):
    exclude = ["user", ]

    def save_model(self, request, obj, form, change):
        if obj is not None:
            obj.user = request.user

        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        return obj and obj.user == request.user

    def has_delete_permission(self, request, obj=None):
        return False


class AirlinePilotInline(admin.StackedInline):
    model = AirlinePilots
    extra = 1


class AirlineAdmin(admin.ModelAdmin):
    inlines = [AirlinePilotInline]

    list_display = ["name"]


class PilotAdmin(admin.ModelAdmin):
    list_display = ["name", "last_name"]


admin.site.register(Airline, AirlineAdmin)
admin.site.register(Balloon)
admin.site.register(Pilot, PilotAdmin)
admin.site.register(Flight, FlightAdmin)
