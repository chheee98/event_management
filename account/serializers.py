from django.contrib.auth import get_user_model
from django.db.models.deletion import models
from rest_framework import serializers

user_model = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_model
        fields = [
            "id",
            "username",
            "password",
            "is_organizer",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = user_model.objects.create_user(**validated_data)
        return user
