# consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from main.models import CustomUser
from .models import Message,Room

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Extract room name from URL and create a group name
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Accept WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Receive message from WebSocket
        data = json.loads(text_data)
        message = data['message']

        await self.save_message(data['username'], data['roomname'], message)
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        # Send message to WebSocket
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))
        
    @sync_to_async
    def save_message(self, username, room, message):
        user = CustomUser.objects.get(username = username)
        room = Room.objects.get(slug = room)
        message = Message.objects.create(user=user, room=room, content=message)
        