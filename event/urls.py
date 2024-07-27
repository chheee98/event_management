from rest_framework import routers
from event.views import EventRegistrationView, EventView
from django.urls import include, path

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"event", EventView, basename="Event")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "event_registeration",
        EventRegistrationView.as_view(),
        name="Event Registration",
    ),
]
