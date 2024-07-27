from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.mixins import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.schemas.coreapi import serializers
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from account.serializers import UserSerializer
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

user_model = get_user_model()

class AccountListView(generics.ListAPIView):
    model = user_model
    queryset = user_model.objects.all()
    serializer_class = UserSerializer

class AccountRegisterView(generics.CreateAPIView):
    model = user_model
    queryset = user_model.objects.all()
    serializer_class = UserSerializer


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            if not refresh_token:
                raise serializers.ValidationError("Refresh token is required.")

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=205)
        except (InvalidToken, TokenError) as e:
            return Response(status=400, data={"error": str(e)})
