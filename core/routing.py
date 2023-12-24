from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path("/ws/event/<event>", consumers.EventsConsumer.as_asgi()),
]
