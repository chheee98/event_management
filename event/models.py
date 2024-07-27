from django.contrib.auth import get_user_model
from django.db import models

from core.models import AbstractBaseModel

user_model = get_user_model()


class Event(AbstractBaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateTimeField()
    location = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField()
    organizer = models.ForeignKey(
        user_model, on_delete=models.CASCADE, related_name="organized_events"
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = "event_event"


class EventRegistration(AbstractBaseModel):
    guest = models.ForeignKey(
        user_model, on_delete=models.CASCADE, related_name="guest_registered_events"
    )
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="event_registered_events"
    )

    class Meta:
        db_table = "event_event_registration"
        unique_together = ("guest", "event")
