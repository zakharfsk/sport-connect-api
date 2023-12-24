from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json


class EventsConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        self.event = self.scope["url_route"]["kwargs"]["event"]
        await self.channel_layer.group_add(self.event, self.channel_name)
        await self.accept()

    async def receive_json(self, content, **kwargs):
        message = content.get('message', '')
        await self.send(text_data=json.dumps({'message': f'{message}'}))

    async def close(self, close_code):
        await self.channel_layer.group_discard(self.event, self.channel_name)
