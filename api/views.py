from django.shortcuts import render
from django.http import JsonResponse
from django.forms import model_to_dict
from stations.models import Genre, RadioList, UserSession, Favourite
from django.db import models
import requests
# Create your views here.
def getAllCategories(request):
    category = Genre.objects.values_list('genre').distinct()
    li = []
    for i in category:
        li.append(i[0].replace("%20", " "))
    data = dict(feed=sorted(li))
    return JsonResponse(data)

def radiosList(request, pk):
    radios = RadioList.objects.filter(radio_genre__genre=pk)
    
    li = []
    for radio in radios:
        genres = []
        n = model_to_dict(radio)
        for i in radio.radio_genre.all():
            genres.append(i.genre)
        n['genre'] = sorted(genres)
        li.append(n)
    
    radio_feed = dict(feed=li)
    return JsonResponse(radio_feed)


def addFavourite(request, pk):
    if not request.session.exists(request.session.session_key):
        request.session.create()
    session = UserSession.objects.filter(session=request.session.session_key)
    if session.exists():
        session = session[0]
    else:
        session = UserSession(session=request.session.session_key)
        session.save()
    radio = RadioList.objects.get(id=pk)
    fav = Favourite.objects.filter(radio=radio, session=session)
    if not fav.exists():
        f = Favourite(radio=radio, session=session)
        f.save()
    return JsonResponse({"message" : "Radio Added"})

def removeFavourite(request, pk):
    if not request.session.exists(request.session.session_key):
        request.session.create()
    session = UserSession.objects.filter(session=request.session.session_key)
    if session.exists():
        session = session[0]
    else:
        session = UserSession(session=request.session.session_key)
        session.save()
    radio = RadioList.objects.get(id=pk)
    fav = Favourite.objects.filter(radio=radio, session=session)
    fav[0].delete()
    return JsonResponse({"message" : "Radio Added"})

def FavouriteList(request):
    if not request.session.exists(request.session.session_key):
        request.session.create()
    session = UserSession.objects.filter(session=request.session.session_key)
    fav = Favourite.objects.filter(session=session[0])

    li = []

    for radio in fav:
        n = model_to_dict(radio.radio)
        genres = []
        for i in radio.radio.radio_genre.all():
            genres.append(i.genre)
        n['genre'] = sorted(genres)

        li.append(n)
    radio_feed = dict(feed=li)
    return JsonResponse(radio_feed)


def getSearches(requests, pk):
    radios = RadioList.objects.filter(radio_name__contains=pk).order_by("?")[:3]
    li = []
    for i in radios:
        n = model_to_dict(i)
        n.pop("radio_img", None)
        li.append(n)
    feed = dict(feed=li)
    return JsonResponse(feed)

def getRandomRadio(request):
    radio = RadioList.objects.all().order_by('?')[0]
    rad = dict(radio_id=radio.id, radio_name=radio.play_link, link=radio.radio_name)
    return JsonResponse(rad)

def deleteCat(request):
    for radio in RadioList.objects.all():
        if radio.play_link == "":
            radio.delete()

def getCountries(request):
    response = requests.get("https://slusajradio.live/api/getCountries")
    return JsonResponse(response.json())
