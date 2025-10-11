from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Call
from .utils import send_webhook_notification


@receiver(post_save, sender=Call)
def call_created_handler(sender, instance, created, **kwargs):
    """
    Trigger webhook when a new Call is created.
    Sends detailed info including hospital, room, and floor context.
    """
    if created:
        data = {
            "call_id": instance.id,
            "room_no": instance.patient.room_number,
            "hospital_name": instance.room.hospital.name if instance.room.hospital else None,
            #"city": instance.room.hospital.city if instance.room.hospital else None,
            "floor_no": instance.room.floor_no,
            "call_from": instance.call_from,
            "created_at": instance.created_at.isoformat(),
        }

        # Send webhook notification with enriched data
        send_webhook_notification(data)
