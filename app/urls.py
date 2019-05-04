from django.conf.urls import url
 
from . import views
from django.contrib.auth.decorators import login_required
 
urlpatterns = [
	url(r'^$', views.home),
    url(r'^$voyage', views.voyage),
    url(r'^$blog', views.blog)
]
