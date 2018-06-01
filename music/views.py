from django.http import HttpResponse
from .models import Album

def index(request):
    #a variable that gets all the albums by connection to database
    all_album=Album.objects.all()
    html=''

    for album in all_album:
        url=',/music/'+str(album.id)+'/'
        html+='<a href="'+url+'"">'+album.album_title+'<a><br>'

    return HttpResponse(html)

def detail(request,album_id):
    return HttpResponse("<h2>Details for Album Id :"+str(album_id)+"</h2>")
