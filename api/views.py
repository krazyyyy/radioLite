from django.shortcuts import render
from django.http import JsonResponse
from django.forms import model_to_dict
from stations.models import Genre, RadioList
from django.db import models

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


def getRandomRadio(request):
    radio = RadioList.objects.all().order_by('?')[0]
    rad = dict(radio_id=radio.id, radio_name=radio.play_link, link=radio.radio_name)
    return JsonResponse(rad)

def deleteCat(request):
   for row in RadioList.objects.all().reverse()[:5]:
       print(row.radio_genre.all())
        # row.delete()