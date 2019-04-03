from django.conf.urls import url
 
from . import views
from . import apis
from django.contrib.auth.decorators import login_required
 
urlpatterns = [
	url(r'^$', views.index),
	url(r'^api/getWeather', apis.getWeather),
	url(r'^api/sendMessage', apis.sendMessage)
]
