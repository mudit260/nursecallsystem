from django.urls import path
from . import views

urlpatterns = [
    # ---- Call Management ----
    path("call/", views.create_call, name="create_call"),  # POST
    path("call/<int:pk>/ack/", views.acknowledge_call, name="ack_call"),  # POST
    path("call/<int:pk>/attend/", views.attend_call, name="attend_call"),  # POST
    path("calls/unacknowledged/", views.unacknowledged_calls, name="unack_calls"),  # GET
    path("calls/events/", views.call_events, name="call_events"),  # GET

    # ---- Room Management ----
    path("rooms/", views.list_rooms, name="list_rooms"),  # GET
    path("rooms/create/", views.create_room, name="create_room"),  # POST

    # ---- Webhook ----
    path("webhook/", views.webhook_receiver, name="webhook_receiver"),  # POST

    # ---- Hospital Management ----
    path("hospitals/", views.list_hospitals, name="list_hospitals"),  # GET
    path("hospitals/create/", views.create_hospital, name="create_hospital"),  # POST
]
