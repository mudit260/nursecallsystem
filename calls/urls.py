from django.urls import path
from . import views

urlpatterns = [
    # ---- Call Management ----
    path("call/", views.create_call, name="create_call"),
    path("call/<int:pk>/ack/", views.acknowledge_call, name="ack_call"),
    path("call/<int:pk>/attend/", views.attend_call, name="attend_call"),

    # ---- Room Management ----
    path("rooms/", views.list_rooms, name="list_rooms"),
    path("rooms/create-random/", views.create_random_rooms, name="create_random_rooms"),
    path("calls/unacknowledged/", views.unacknowledged_calls, name="unack_calls"),

    # ---- Webhook ----
    path("webhook/", views.webhook_receiver, name="webhook_receiver"),

    # ---- Hospital Management (NEW) ----
    path("hospitals/", views.list_hospitals, name="list_hospitals"),
    path("hospitals/create/", views.create_hospital, name="create_hospital"),
    path("hospitals/", views.list_hospitals, name="list_hospitals"),
    path("hospitals/create/", views.create_hospital, name="create_hospital"),
    path("calls/events/", views.call_events, name="call_events"),

]
