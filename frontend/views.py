from django.shortcuts import render
from django.http import JsonResponse
import csv

from stations.models import RadioList, Genre, Countries
# Create your views here.
def index(request):
    return render(request, 'frontend/index.html', {
        "country" : Countries.objects.get(id=1)
    })

def explore(request):
    return render(request, 'frontend/explore.html', {
        "country" : Countries.objects.get(id=1)
    })

def genre(request, pk):
    return render(request, 'frontend/genre.html', {
        "keyword" : pk,
        "country" : Countries.objects.get(id=1)
    })

def favouritePage(request):
    country = Countries.objects.get(id=1)
    return render(request, 'frontend/favourite.html', {
        "country" : country
    })

def search(request):
    pk = request.POST.get("keyword")
    countryOBJ = Countries.objects.get(id=1)
    radios = RadioList.objects.filter(play_link__contains=pk)
    
    return render(request, 'frontend/search.html', {
        'radios' : radios,
        'country' : countryOBJ
    })

def popularPage(request):
  
    radios = RadioList.objects.all().order_by("?")[:20]
    
    return render(request, 'frontend/popular.html', {
        'radios' : radios,
        'country' : Countries.objects.get(id=1)
    })

def latestPage(request):
  
    radios = RadioList.objects.all().order_by("-id")[:20]
    
    return render(request, 'frontend/popular.html', {
        'radios' : radios,
        'country' : Countries.objects.get(id=1)
    })


def radioPlayerPage(request, pk, title):
    radio = RadioList.objects.get(id=pk)
    return render(request, 'frontend/radioPlayer.html', {
        "radio" : radio,
        "country" : Countries.objects.get(id=1)
    })

def create(request):
    with open("RadioData.csv", "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for i in reader:
            radio = RadioList(radio_name=i[0], play_link=i[1])
            radio.save()


            str_list = filter(lambda item: item, i[2].split("|"))
            str_list = list(filter(None, str_list))
            for li in str_list:
                genre = Genre(genre=li, radio=radio)
                genre.save()
    
    return JsonResponse({"Message" : "Success"})


