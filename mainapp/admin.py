from django.contrib import admin
from .models import Room, Topic, Message


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'host', 'topic', 'updated')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'body', 'user', 'room', 'updated')
