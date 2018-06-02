from django.conf.urls import include, url
from . import views
#from django.contrib import admin

app_name='music'

urlpatterns = [
        # for music home
    url(r'^$', views.index , name='index'),

        #for music home/AlbumId/
        #[0-9] tells that the id we will be receiving is a number and the + after indicates the this would be a long integer
    url(r'^(?P<album_id>[0-9]+)/$', views.detail , name='detail'),

    url(r'^register/$', views.UserFormView.as_view() , name='register'),

    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite , name='favorite'),
]
