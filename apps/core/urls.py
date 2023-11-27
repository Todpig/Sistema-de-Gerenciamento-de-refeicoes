from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("today-menu", TodayMenu.as_view(), name="todayMenu"),
    path("request-snack", RequestSnackView.as_view(), name="request-snack"),
    path("all-request-meal", AllRequestMealView.as_view(), name="all-request-meal"),
    path("create-meal", FormToCreateMealView.as_view(), name="create-meal"),
    path("select-dish", SelectDishView.as_view(), name="select-dish"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]