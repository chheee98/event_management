from rest_framework import filters
from rest_framework.settings import api_settings
from rest_framework import generics, serializers, viewsets
from rest_framework.permissions import BasePermission
from event.models import Event, EventRegistration
from event.serializers import (
    EventRegistrationSerializer,
    EventRetrieveSerializer,
    EventSerializer,
)

DEFAULT_FILTER_BACKEND = getattr(api_settings, "DEFAULT_FILTER_BACKENDS", [])


class IsOrganizerUser(BasePermission):
    """
    Allows access only to Organizer users.
    """

    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated and request.user.is_organizer
        )


class EventView(viewsets.ModelViewSet):
    model = Event
    queryset = Event.objects.all().order_by('-event_date')
    serializer_class = EventSerializer
    filter_backends = DEFAULT_FILTER_BACKEND + [filters.SearchFilter]
    filterset_fields = ["title", "event_date", "location"]
    search_fields = ["title", "description", "location"]
    permission_classes = [IsOrganizerUser]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return EventRetrieveSerializer

        return super().get_serializer_class()

    def perform_create(self, serializer):
        if "organizer" not in serializer.validated_data:
            serializer.validated_data["organizer"] = self.request.user

        serializer.save()


class EventRegistrationView(generics.CreateAPIView):
    model = EventRegistration
    queryset = EventRegistration.objects.all()
    serializer_class = EventRegistrationSerializer

    def perform_create(self, serializer):
        event = serializer.validated_data["event"]

        if EventRegistration.objects.filter(event=event).count() >= event.capacity:
            raise serializers.ValidationError("This event is full.")

        if not serializer.validated_data.get("guest"):
            serializer.validated_data["guest"] = self.request.user

        if event.organizer == serializer.validated_data["guest"]:
            raise serializers.ValidationError("Organizer cannot join their event.")

        serializer.save()
