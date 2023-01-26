from django.urls import path
from .views import (
    room,lobby
)

urlpatterns = [
    path('',lobby,name="Lobby"),
    path('room/',room,name="Room"),
]