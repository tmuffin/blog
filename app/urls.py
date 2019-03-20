from django.conf.urls import url
 
from . import views
from . import apis
 
urlpatterns = [
	url(r'^$', views.index),
	url(r'^api/getWeather', apis.getWeather),
	url(r'^api/sendMessage', apis.sendMessage)
]
