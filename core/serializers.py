from django.contrib.auth import get_user
from rest_framework import serializers
from core.models import AbstractBaseModel


class BaseSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = self._get_user()
        if user and issubclass(self.Meta.model, AbstractBaseModel):
            validated_data["create_by"] = user
            validated_data["write_by"] = user

        return super().create(validated_data)

    def update(self, instance, validated_data):
        user = self._get_user()
        if user and issubclass(self.Meta.model, AbstractBaseModel):
            validated_data["write_by"] = user

        return super().update(instance, validated_data)

    def _get_user(self):
        if "request" in self.context:
            return self.context["request"].user
