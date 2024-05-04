from django.urls import path,include
from . import views

# from .consumers import ChatConsumer

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('<slug:slug>/', views.room, name='room'),
    # path('ws/<str:>/', ChatConsumer.as_asgi(), name='room')
    path('', include('room.routing'))
]