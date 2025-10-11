from django.db import models
from django.utils import timezone
import random


class Hospital(models.Model):
    name = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=100, blank=True, null=True)  # optional
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.city})" if self.city else self.name



class Room(models.Model):
    room_no = models.CharField(max_length=10)
    floor_no = models.IntegerField()
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name="rooms")
    acknowledged = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("room_no", "floor_no", "hospital")  # same room_no allowed on different floors/hospitals

    def __str__(self):
        return f"{self.hospital.name} - Floor {self.floor_no} - Room {self.room_no}"


    @staticmethod
    def create_random_rooms(hospital=None, n=20):
        """Generate N random rooms (100–999) for a hospital."""
        if not hospital:
            hospital, _ = Hospital.objects.get_or_create(name="Default Hospital")

        for i in range(n):
            room_no = str(random.randint(100, 999))
            floor_no = random.randint(1, 5)
            Room.objects.get_or_create(
                hospital=hospital,
                room_no=room_no,
                defaults={"floor_no": floor_no}
            )


class Call(models.Model):
    room_no = models.CharField(max_length=10)
    floor_no = models.IntegerField()
    hospital_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    call_from = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

    acknowledged_at = models.DateTimeField(null=True, blank=True)
    attended_at = models.DateTimeField(null=True, blank=True)
    response_time_seconds = models.IntegerField(null=True, blank=True)
    attend_delay_seconds = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # calculate response_time_seconds
        if self.acknowledged_at and not self.response_time_seconds:
            self.response_time_seconds = int((self.acknowledged_at - self.created_at).total_seconds())
        # calculate attend_delay_seconds
        if self.attended_at and not self.attend_delay_seconds:
            if self.acknowledged_at:
                self.attend_delay_seconds = int((self.attended_at - self.acknowledged_at).total_seconds())
            else:
                self.attend_delay_seconds = int((self.attended_at - self.created_at).total_seconds())
        super().save(*args, **kwargs)


    def __str__(self):
        return f"Call from {self.room} at {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
