import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.shortcuts import get_object_or_404
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework.views import APIView  

from .models import Call, Room
from .webhooks import send_webhook
from .serializers import CallSerializer, RoomSerializer, HospitalSerializer
# ✅ Logger for Render logs
logger = logging.getLogger(__name__)


class CallViewSet(APIView):
    def post(self, request):
        logger.info("📞 Received new call POST request")
        serializer = CallSerializer(data=request.data)

        if serializer.is_valid():
            call = serializer.save()

            payload = {
                "id": call.id,
                "room_no": call.room.room_no if call.room else None,
                "hospital_name": getattr(call.room.hospital, "name", None),
                "city": getattr(call.room.hospital, "city", None),
                "floor_no": getattr(call.room, "floor_no", None),
                "call_from": call.call_from,
                "created_at": str(call.created_at),
                "status": "New call received"
            }

            logger.info(f"🚀 Sending webhook for new call: {payload}")
            send_webhook(payload)

            logger.info(f"✅ Call created successfully (ID: {call.id})")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            logger.error(f"❌ Invalid call data: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def send_ws_notification(event_type, call):
    """Push real-time WebSocket notifications"""
    channel_layer = get_channel_layer()
    content = {
        "event": event_type,
        "call_id": call.id,
        "room_no": call.room.room_no if call.room else None,
        "hospital_name": getattr(call.room.hospital, "name", None),
        "city": getattr(call.room.hospital, "city", None),
        "floor_no": getattr(call.room, "floor_no", None),
        "call_from": call.call_from,
        "created_at": call.created_at.isoformat(),
        "acknowledged_at": call.acknowledged_at.isoformat() if call.acknowledged_at else None,
        "attended_at": call.attended_at.isoformat() if call.attended_at else None,
    }

    logger.info(f"📡 Sending WebSocket notification: {content}")
    async_to_sync(channel_layer.group_send)(
        "notifications",
        {"type": "notify", "content": content}
    )


@api_view(["POST"])
def create_call(request):
    serializer = CallSerializer(data=request.data)
    if serializer.is_valid():
        call = serializer.save()

        # Send webhook / websocket
        payload = {
            "call_id": call.id,
            "room_no": call.room_no,
            "floor_no": call.floor_no,
            "hospital_name": call.hospital_name,
            "city": call.city,
            "call_from": call.call_from,
            "created_at": str(call.created_at),
            "status": "New call received"
        }
        send_webhook(payload)
        send_ws_notification("call_created", call)
        return Response(CallSerializer(call).data, status=201)
    return Response(serializer.errors, status=400)



@api_view(["POST"])
def acknowledge_call(request, pk):
    logger.info(f"👩‍⚕️ Nurse acknowledged call ID: {pk}")
    call = get_object_or_404(Call, pk=pk)

    if not call.acknowledged_at:
        call.acknowledged_at = timezone.now()
        call.response_time_seconds = int((call.acknowledged_at - call.created_at).total_seconds())
        call.save()

        logger.info(f"✅ Call acknowledged at {call.acknowledged_at}")
        send_ws_notification("call_acknowledged", call)
        send_webhook({
            "event": "call_acknowledged",
            "call_id": call.id,
            "acknowledged_at": str(call.acknowledged_at)
        })

    return Response(CallSerializer(call).data, status=status.HTTP_200_OK)


@api_view(["POST"])
def attend_call(request, pk):
    logger.info(f"🚶‍♀️ Nurse attending call ID: {pk}")
    call = get_object_or_404(Call, pk=pk)

    if not call.attended_at:
        call.attended_at = timezone.now()
        if call.acknowledged_at:
            call.attend_delay_seconds = int((call.attended_at - call.acknowledged_at).total_seconds())
        else:
            call.attend_delay_seconds = int((call.attended_at - call.created_at).total_seconds())
        call.save()

        logger.info(f"✅ Call attended at {call.attended_at}")
        send_ws_notification("call_attended", call)
        send_webhook({
            "event": "call_attended",
            "call_id": call.id,
            "attended_at": str(call.attended_at)
        })

    return Response(CallSerializer(call).data, status=status.HTTP_200_OK)


@api_view(["GET"])
def unacknowledged_calls(request):
    logger.info("📋 Fetching unacknowledged calls list")
    calls = Call.objects.filter(acknowledged_at__isnull=True).order_by("created_at")
    return Response(CallSerializer(calls, many=True).data)



@api_view(["POST"])
def create_room(request):
    """
    Create a room with proper hospital and floor
    Payload example: {
        "room_no": "101",
        "floor_no": 3,
        "hospital": 1
    }
    """
    serializer = RoomSerializer(data=request.data)
    if serializer.is_valid():
        room = serializer.save()
        return Response(RoomSerializer(room).data, status=201)
    return Response(serializer.errors, status=400)


@api_view(["GET"])
def list_rooms(request):
    logger.info("📋 Listing all rooms")
    rooms = Room.objects.all().order_by("room_no")
    return Response(RoomSerializer(rooms, many=True).data)


@api_view(["POST"])
def webhook_receiver(request):
    """
    Receives webhook notifications from this or other services
    """
    data = request.data
    logger.info(f"📩 Webhook received: {data}")
    return Response({"status": "received"}, status=status.HTTP_200_OK)
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def list_hospitals(request):
    hospitals = [
        {"name": "Fortis"},
        {"name": "Apollo"},
        {"name": "City Hospital"},
    ]
    return Response(hospitals)

HOSPITALS = []

@api_view(["POST"])
def create_hospital(request):
    serializer = HospitalSerializer(data=request.data)
    if serializer.is_valid():
        hospital = serializer.save()
        return Response(HospitalSerializer(hospital).data, status=201)
    return Response(serializer.errors, status=400)

# --- your existing imports and views stay unchanged above ---

@api_view(["GET"])
def call_events(request):
    """
    Returns all call events with optional filtering by hospital, floor_no, or room_no.
    Query params (optional):
      - hospital: string
      - floor_no: int
      - room_no: string
    """
    hospital = request.query_params.get("hospital")
    floor_no = request.query_params.get("floor_no")
    room_no = request.query_params.get("room_no")

    calls = Call.objects.select_related("room").all()

    if hospital:
        calls = calls.filter(hospital_name__iexact=hospital)
    if floor_no:
        try:
            floor_int = int(floor_no)
            calls = calls.filter(floor_no=floor_int)
        except ValueError:
            logger.warning(f"Invalid floor_no value: {floor_no}")
    if room_no:
        calls = calls.filter(room_no=room_no)
        logger.info(f"Filtering calls by room_no={room_no}")

    serializer = CallSerializer(calls, many=True)
    logger.info(f"Returning {len(serializer.data)} call events")
    return Response(serializer.data)
