from rest_framework import serializers
from .models import Hospital, Room, Call


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ["id", "name"]

class RoomSerializer(serializers.ModelSerializer):
    hospital_name = serializers.CharField(source="hospital.name", read_only=True)
    #hospital_city = serializers.CharField(source="hospital.city", read_only=True)

    class Meta:
        model = Room
        fields = ["id", "room_no", "floor_no", "hospital", "hospital_name", "acknowledged", "created_at"]


class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = [
            "id",
            "room_no",
            "floor_no",
            "hospital_name",
            #"city",
            "call_from",
            "created_at",
            "acknowledged_at",
            "attended_at",
            "response_time_seconds",
            "attend_delay_seconds",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "acknowledged_at",
            "attended_at",
            "response_time_seconds",
            "attend_delay_seconds",
        ]
