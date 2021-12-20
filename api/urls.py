from django.urls import path

from . import views

urlpatterns = [
    path("categories", views.getAllCategories, name="categories"),
    path("radios/<str:pk>", views.radiosList, name="radios"),
    path("getRandomRadio", views.getRandomRadio, name="getRandomRadio"),
    path("delete", views.deleteCat, name="deleteCat"),
    
]