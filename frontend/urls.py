from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("genre/<str:pk>", views.genre, name="genre"),
    path("radioPlayer/<str:pk>/<str:title>", views.radioPlayerPage, name="radioPlayerPage"),
]