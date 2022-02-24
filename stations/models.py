from django.db import models
from django.urls import reverse
# Create your models here.
class Countries(models.Model):
    country_name = models.CharField(max_length=200)
    country_flag = models.CharField(max_length=500, null=True, blank=True)
    country_code = models.CharField(max_length=10, null=True, blank=True)
    

    def __str__(self):
        return f"{self.country_name}"

class RadioList(models.Model):
    play_link = models.CharField(max_length=200, null=True, blank=True)
    radio_link = models.CharField(max_length=200, null=True, blank=True)
    radio_name = models.CharField(max_length=200, null=True, blank=True)
    rss_feed = models.CharField(max_length=200, null=True, blank=True)
    popular = models.BooleanField(default=False)
    country = models.ForeignKey('Countries', on_delete=models.CASCADE, related_name="radio_country", null=True, blank=True)

    def get_absolute_url(self):
        return reverse('radioPlayerPage', kwargs={'pk':self.id, 'title' : self.play_link.replace(" ", "-").replace("/", "-")})


class Genre(models.Model):
    genre = models.CharField(max_length=200)
    radio = models.ForeignKey('RadioList', on_delete=models.CASCADE, related_name="radio_genre")

class Category(models.Model):
    category = models.CharField(max_length=200)
    radio = models.ForeignKey('RadioList', on_delete=models.CASCADE, related_name="radio_category")

class RadioHistory(models.Model):
    session = models.CharField(max_length=200)
    radio = models.ForeignKey(RadioList, related_name="radio", on_delete=models.CASCADE)

class RadioSession(models.Model):
    name = models.CharField(max_length=200)
    img_link = models.CharField(max_length=200, null=True, blank=True)
    history = models.ForeignKey('RadioHistory', related_name="radio_history_session", on_delete=models.CASCADE)

class RssFeed(models.Model):
    source = models.CharField(max_length=200)
    source_id = models.ForeignKey(RadioList, null=True, blank=True, on_delete=models.CASCADE, related_name="source_radio")
    link = models.CharField(max_length=500)
    title = models.CharField(max_length=200)
    pub_date = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    country = models.ForeignKey('Countries', on_delete=models.CASCADE, related_name="radioCountryFeed", null=True, blank=True)

class AD_Zones(models.Model):
    sidebarAD = models.TextField(null=True, blank=True,  help_text="Left SideBar Ad")
    newsSideAD = models.TextField(null=True, blank=True,  help_text="News Sidebar Ad")
    home_ad = models.TextField(null=True, blank=True,  help_text="add between radio")
    radio_ad = models.TextField(null=True, blank=True,  help_text="add between radio")
    access_name =  models.CharField(max_length=10, default="admin")

    def __str__(self):
        return f"Manage ADs"

class UserSession(models.Model):
    session = models.CharField(max_length=350)


class Favourite(models.Model):
    radio = models.ForeignKey(RadioList, on_delete=models.CASCADE, related_name="favourite_radio")
    session = models.ForeignKey('UserSession', on_delete=models.CASCADE, related_name="userSession")
    