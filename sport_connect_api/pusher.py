from django.conf import settings
from pusher import Pusher

pusher = Pusher(
    app_id=settings.PUSHER_APP_ID,
    key=settings.PUSHER_KEY,
    secret=settings.PUSHER_SECRET,
    cluster=settings.PUSHER_CLUSTER,
    ssl=True
)


def trigger_event(channel: str, event: str, data: dict):
    pusher.trigger(channel, event, data)
