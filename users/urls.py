from django.urls import path
from users.views import login, registration, profile, logout, users_basket


app_name = "users"

urlpatterns = [
    path("login/", login, name="login"),
    path("registration/", registration, name="registration"),
    path("profile/", profile, name="profile"),
    path("logout/", logout, name="logout"),
    path("users-basket", users_basket, name="users-basket"),
]
