## What are these files

manage.py is a program with django , like manager
__init__.py means the directory is a python package
settings.py it is overall settings of website
urls.py     it tells to return a function,page to request


## django commands

django-admin startproject Xpiarance //to start project
		[__init__  tells python that it is a python package]
python manage.py runserver//to run the localhost
python manage.py startapp music	//to make an app
		[`migrations` connect your website with database]
		[apps are the configuraton files]
		[models are templates (Blueprints) for database
		Lets assume what tables we want in our database
		like music has Albums , Songs]
		[tests are for checking bugs]
		[views performs and sends response for a user request]
python manage.py makemigrations music [after making apps.py for music and listing in settings.py of the tutorial]
### Website/urls.py

		whenever a user makes a request , django searches for the urlpatterns
		url(r'^admin/',admin.site.urls) second is the response
		Since there would be many users and many people using the site it would be much easier if we make a urls.py in the music folder. Try to make everything related to app in the apps' directory only.

### music/urls.py
		copy paste.

		from . import views //wehenever something user requests we send response so we need to import so that we could use the things of views to use in the response.

		url(r'^$', views.index , name='index')// '$' sign here means homepage. https://site.com/music/ nothing after that.	views.index is the thing to  be returned.

		Now the website/urls.py does not knows about the music/urls so we do some changes.

		from django.conf.urls import include, url #include do help to know about the other files also.

		url(r'^music/', include('music.urls')), add this code it tells that if anything starts with https://site.com/music music then repond to music.url

### music/views.py
		clear the views.py

		views sends the Http response so add this
		from django.http import HttpResponse

		now make a function named as index
		index(request):
		    return HttpResponse("Things to display here")


# CrEATING database
		On line 77 of settings.py you will find that the default database is "sqlite3"

		Now we need to configure the databaase with the code

		On lne 33 you can find that there are bunch of apps ready to use.

		Our code is not yet in sync with the databases
		`python manage.py migrate` to sync it.
		Actual happening behind the scene is that it goes to the INSTALLED_APPS in settings.py and see each and every app then it tries to look that what tables each app needs and it sets up the tables.

# Creating models
		Like our app need titles, songs, artist ,genre

		So we need to create database.

		It gets each variable from the code and converts it to a column in the database.

		Now create class Album.
		every Blueprint you create is inherited from the modelsss.Models

		`artist = models.CharField(max_length=100)` here artist is the variable here , CharField() tells that what type of data will the variable will hold in database.

		`album - models.ForeignKey(Albumn,on_delete=models.CASCADE)` in class songs there are many songs related to one album so we need some type of link for that we use ForeignKey.

		Like we have album of kishhor kumar and his songs so now PrimaryKey of albums is 1 and the ForeignKey of the songs is also 1 in this way they are related.

		on_delete=models.CASCADE means that since if you delete the whole albums the songs also need to be deleted.

		PrimaryKey is the unique key for each and every album in database . Like there may be many albumns with same name so ther is unique ID to avoid any such mess.

		Now we have made a app so now list it in the list of INSTALLED_APPS .
		`'music.apps.MusicConfig'`

		Make a apps.py and code it.

		Now we have made everything ready except one thing we haven't reflected it yet in our database.

`python manage.py makemigrations music`
after making apps.py for music and listing in settings.py .
It tels that we  have made some changes in the models.py and now we need to reflect it in our database.

`python manage.py migrate` to execute the changes


Next are not necessary
python manage.py sqlmigrate music 0001//
		[migration means change in database]
		[creates tablesin databse]
python manage.py migrate //py


# Database API
		Now we will learn something about the database
		here are the ```
		pyhton manage.py shell //to open workspace

		from music.models import Album,Song // to import the things stored.

		Album.objects.all() // to view al the objects of the class Albums.

		a=Album(artist="Lata Mangeshkar" , album_title="Deshbhakti" , genre="Patriotic" , album_logo="https://s1-ssl.dmcdn.net/DmitP/x720-0Sx.jpg")	//to make an object

		a.save //to save the databse

		--------------OR-----------------

		b=Album()
		b.artist='Taylor Swift'
		b.album_logo="someurl.in/img.png"

		//Now when you use it shows all the albums in the databsase
		Album.objects.all()
		```

		But the things stored in database are not fully listed when tou want to see it.
		So we will build a new function now in models.py

		```
		def __str__(self):
	        return self.album_title+'-'+self.artist
		```

		This helps to return a string giving the things stored.

		`Album.objects.filter(id=2)`
		Gives the album with pk is 2.

# admin
		python manage.py createsuperuser //creates a sueruser which has access to the database

		But we still don't have access to our other things we stored using shell.

		Goto music/admin.py
		`from .models import Album`
		This tells the admin that it has now access to the Album just like w
		Now search e did in the shell.
		Also register the Album.

# Adding another webpage
		//for music home/AlbumId/
		//[0-9] tells that the id we will be receiving is a number and the + after indicates the this would be a long integer
`url(r'^(?P<album_id>[0-9]+)$', viwes.detail , name='detail')`
		It requests for details in view so make a function there Also

		In views add
		```def detail(request,album_id):
		    return HttpResponse("<h2>Details for Album Id :"+str(albumId)"</h2>")

		```
		Now search ```http://127.0.0.1:8000/music/1/```
		You can search all these but still there is no verification yet as it is not connected to the database. Now we need to verify the availibilty.

		Add this in the views
		`from .models import Album`

		```def index(request):
		    #a variable that gets all the albums by connection to database
		    all_album=Album.objects.all()
		    html=''	#simply a variable

		    for album in all_album:
		        url=',/music/'+str(album.id)+'/'
		        html+='<a href="'+url+'"">'+album.album_title+'<a><br>'

		    return HttpResponse("html)

		```

# seprating the html from python
