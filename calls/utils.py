import json
import requests
import logging
from django.conf import settings

logger = logging.getLogger(__name__)

def send_webhook_notification(call):
    """
    Sends a webhook notification to the backend or an external service
    whenever a Call is created.
    """

    # Build structured payload including hospital & floor info
    payload = {
        "room_no": call.room.room_no if call.room else None,
        "floor_number": getattr(call.room, "floor_number", None),
        "hospital_name": getattr(call.room, "hospital_name", None),
        "call_from": call.call_from,
        "created_at": call.created_at.isoformat(),
        "status": "new_call"
    }

    # Define your webhook URL (can also be moved to Django settings)
    webhook_url = getattr(settings, "WEBHOOK_URL", "https://nursecallsystem.onrender.com/api/webhook/")

    logger.info(f"🚀 Sending webhook to {webhook_url} with payload: {json.dumps(payload)}")

    try:
        response = requests.post(
            webhook_url,
            data=json.dumps(payload),
            headers={"Content-Type": "application/json"},
            timeout=5
        )

        # Raise for HTTP errors (e.g., 4xx, 5xx)
        response.raise_for_status()

        logger.info(f"✅ Webhook sent successfully! Status: {response.status_code}")
        logger.info(f"🔁 Webhook response: {response.text[:200]}")

    except requests.exceptions.Timeout:
        logger.error("⏰ Webhook request timed out!")
    except requests.exceptions.RequestException as e:
        logger.error(f"❌ Webhook send failed: {e}")
