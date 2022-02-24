from django.urls import path

from . import views

urlpatterns = [
    path("categories", views.getAllCategories, name="categories"),
    path("radios/<str:pk>", views.radiosList, name="radios"),
    path("getRandomRadio", views.getRandomRadio, name="getRandomRadio"),
    path("getCountries", views.getCountries, name="getCountries"),
    path("delete", views.deleteCat, name="deleteCat"),
    path("getSearches/<str:pk>", views.getSearches, name="getSearches"),
    path("addFavourite/<str:pk>", views.addFavourite, name="addFavourite"),
    path("removeFavourite/<str:pk>", views.removeFavourite, name="removeFavourite"),
    path("FavouriteList", views.FavouriteList, name="FavouriteList"),
]