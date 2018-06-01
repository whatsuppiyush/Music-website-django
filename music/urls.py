from django.conf.urls import include, url
from . import views
#from django.contrib import admin

urlpatterns = [
        # for music home
    url(r'^$', views.index , name='index'),

        #for music home/AlbumId/
        #[0-9] tells that the id we will be receiving is a number and the + after indicates the this would be a long integer
    url(r'^(?P<album_id>[0-9]+)/$', views.detail , name='detail'),
]
