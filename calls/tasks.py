from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import Call
import logging

logger = logging.getLogger(__name__)


@shared_task
def notify_unacknowledged_calls():
    """
    Celery task to detect calls that haven't been acknowledged within 3 minutes
    and send real-time WebSocket + log notifications.
    """
    threshold = timezone.now() - timedelta(minutes=3)
    unacked_calls = Call.objects.filter(
        acknowledged_at__isnull=True,
        created_at__lte=threshold
    )

    channel_layer = get_channel_layer()

    if not unacked_calls.exists():
        logger.info("✅ No unacknowledged calls older than 3 minutes.")
        return

    for call in unacked_calls:
        try:
            hospital = getattr(call.room.hospital, "name", None)
            city = getattr(call.room.hospital, "city", None)
            floor_no = getattr(call.room, "floor_no", None)

            content = {
                "event": "call_unacknowledged",
                "call_id": call.id,
                "room_no": call.room.room_no,
                "hospital_name": hospital,
                "city": city,
                "floor_no": floor_no,
                "created_at": call.created_at.isoformat(),
                "alert": "⚠️ Call not acknowledged for more than 3 minutes!"
            }

            # Send over WebSocket group
            async_to_sync(channel_layer.group_send)(
                "notifications",
                {"type": "notify", "content": content}
            )

            # Log in Render logs
            logger.warning(
                f"🚨 Unacknowledged Call Alert | Room {call.room.room_no} "
                f"({hospital or 'Unknown Hospital'}, Floor {floor_no}) "
                f"- Created at {call.created_at}"
            )

        except Exception as e:
            logger.error(f"❌ Error sending unacknowledged call alert for Call {call.id}: {e}")
