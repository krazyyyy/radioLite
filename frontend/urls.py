from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("explore", views.explore, name="explore"),
    path("create", views.create, name="create"),
    path("genre/<str:pk>", views.genre, name="genre"),
    path("radioPlayer/<str:pk>/<str:title>", views.radioPlayerPage, name="radioPlayerPage"),
    path("search", views.search, name="search"),
    path("popular", views.popularPage, name="popular"),
    path("latest", views.latestPage, name="latestPage"),
    path("favourites", views.favouritePage, name="favouritePage"),
]