from django.db import models

from main.models import CustomUser

class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add= True)
    
    class Meta:
        ordering = ('date_added',)