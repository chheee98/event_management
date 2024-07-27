from rest_framework import serializers
from core.serializers import BaseSerializer
from event.models import Event, EventRegistration


class EventSerializer(BaseSerializer):
    guest_count = serializers.SerializerMethodField()

    def get_guest_count(self, instance):
        return instance.event_registered_events.all().count()

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "description",
            "event_date",
            "location",
            "capacity",
            "organizer",
            "guest_count",
        ]
        extra_kwargs = {
            "organizer": {
                "required": False,
                "allow_null": True,
            }
        }


class EventRetrieveSerializer(BaseSerializer):
    guest_count = serializers.SerializerMethodField()
    guests = serializers.SerializerMethodField()

    def get_guest_count(self, instance):
        return instance.event_registered_events.all().count()

    def get_guests(self, instance):
        return [
            event_registered.guest.username
            for event_registered in instance.event_registered_events.all()
        ]

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "description",
            "event_date",
            "location",
            "capacity",
            "organizer",
            "guest_count",
            "guests",
        ]


class EventRegistrationSerializer(BaseSerializer):

    class Meta:
        model = EventRegistration
        fields = [
            "id",
            "guest",
            "event",
            "create_date",
        ]
        extra_kwargs = {
            "guest": {
                "required": False,
                "allow_null": True,
            }
        }
