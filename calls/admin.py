from django.contrib import admin
from .models import Hospital, Room, Call


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    """Admin panel for Hospital"""
    list_display = ("id", "name", "city", "created_at")
    search_fields = ("name", "city")
    ordering = ("name",)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    """Admin panel for Room"""
    list_display = ("room_no", "hospital", "floor_no", "acknowledged", "created_at")
    list_filter = ("hospital", "floor_no", "acknowledged")
    search_fields = ("room_no", "hospital__name")
    ordering = ("hospital", "floor_no", "room_no")


@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    """Admin panel for Call"""
    list_display = (
        "id",
        "room",
        "get_hospital_name",
        "call_from",
        "created_at",
        "acknowledged_at",
        "attended_at",
        "response_time_seconds",
        "attend_delay_seconds"
    )
    list_filter = ("room__hospital", "room__floor_no")
    search_fields = ("room__room_no", "room__hospital__name", "call_from")
    ordering = ("-created_at",)

    def get_hospital_name(self, obj):
        """Show hospital name in Call list"""
        return obj.room.hospital.name
    get_hospital_name.short_description = "Hospital"

    def save_model(self, request, obj, form, change):
        """Ensure calculations are applied"""
        obj.save()
