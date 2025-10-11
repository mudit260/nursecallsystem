import json
import logging
from channels.generic.websocket import AsyncWebsocketConsumer

logger = logging.getLogger(__name__)


class NotificationConsumer(AsyncWebsocketConsumer):
    """
    Handles real-time notifications for nurse call system.
    Joins the 'notifications' group and broadcasts messages
    when calls are created, acknowledged, or attended.
    """

    async def connect(self):
        # Add this connection to the shared 'notifications' group
        await self.channel_layer.group_add("notifications", self.channel_name)
        await self.accept()
        logger.info(f"🟢 WebSocket connected: {self.channel_name}")

        # Optional welcome message
        await self.send(text_data=json.dumps({
            "event": "connection_established",
            "message": "Connected to Nurse Call System WebSocket"
        }))

    async def disconnect(self, close_code):
        # Remove this connection from the group
        await self.channel_layer.group_discard("notifications", self.channel_name)
        logger.info(f"🔴 WebSocket disconnected: {self.channel_name}")

    async def receive(self, text_data=None, bytes_data=None):
        """
        Optional: Handle messages coming *from* the client
        (for testing or acknowledgements).
        """
        if text_data:
            data = json.loads(text_data)
            logger.info(f"📩 Received from client: {data}")

            # You could process incoming messages here
            await self.send(text_data=json.dumps({
                "event": "echo",
                "message": data.get("message", "No message provided")
            }))

    async def notify(self, event):
        """
        Called by group_send to push notifications to all connected clients.
        """
        content = event.get("content", {})
        logger.info(f"📢 Sending notification: {content}")

        await self.send(text_data=json.dumps({
            "event": content.get("event"),
            "hospital": content.get("hospital"),
            "floor_no": content.get("floor_no"),
            "room_no": content.get("room_no"),
            "call_from": content.get("call_from"),
            "created_at": content.get("created_at"),
            "acknowledged_at": content.get("acknowledged_at"),
            "attended_at": content.get("attended_at"),
            "message": f"Notification: {content.get('event')}"
        }))
