from django.contrib import admin
from .models import Hospital, Room, Call


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    """Admin panel for Hospital"""
    list_display = ("id", "name", "created_at")
    search_fields = ("name",)
    


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    """Admin panel for Room"""
    list_display = ("room_no", "hospital", "floor_no", "acknowledged", "created_at")
    list_filter = ("hospital", "floor_no", "acknowledged")
    search_fields = ("room_no", "hospital__name")
    ordering = ("hospital", "floor_no", "room_no")


from django.contrib import admin
from .models import Call, Hospital

@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    # Use actual fields on Call now
    list_display = (
        "id",
        "room_no",
        "hospital_name",
        "floor_no",
        "call_from",
        "created_at",
        "acknowledged_at",
        "attended_at",
        "response_time_seconds",
        "attend_delay_seconds",
    )

    # For filtering, use fields that exist on Call
    list_filter = ("hospital_name", "floor_no", "acknowledged_at", "attended_at")

    search_fields = ("room_no", "hospital_name", "floor_no", "call_from")

    def save_model(self, request, obj, form, change):
        obj.save()


    def get_hospital_name(self, obj):
        """Show hospital name in Call list"""
        return obj.room.hospital.name
    get_hospital_name.short_description = "Hospital"

    def save_model(self, request, obj, form, change):
        """Ensure calculations are applied"""
        obj.save()
