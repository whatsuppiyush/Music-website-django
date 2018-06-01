from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is the first code</h1>")
