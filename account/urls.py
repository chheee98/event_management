from django.urls import include, path
from .views import AccountListView, AccountRegisterView, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
urlpatterns = [
    path("user", AccountListView.as_view(), name="List User"),
    path("register", AccountRegisterView.as_view(), name="register"),
    path("login", TokenObtainPairView.as_view(), name="login"),
    path("refresh_token", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout", LogoutView.as_view(), name="logout"),
]
