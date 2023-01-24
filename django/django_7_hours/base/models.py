from django.db import models
from django.contrib.auth.models import User


# Create your models here


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"Topic ({self.name})"


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=264)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User,related_name='participants', blank=True) # active users in the room
    update = models.DateTimeField(auto_now=True)  # will be updated automatically every time model is updated
    created = models.DateTimeField(auto_now_add=True)  # will be created only the models is saved for the first time

    class Meta:
        ordering = ['-update', '-created']

    def __str__(self):
        return f"Room ({self.name})"


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    # on_delete = models.SET_NULL
    # when the parent is deleted make children null
    # on_delete = models.CASCADE
    # delete all the messages for that room
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']
    def __str__(self):
        return f"{self.body[0:50]}"
