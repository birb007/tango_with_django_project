from django.http import HttpResponse

def index(response):
    return HttpResponse("Rango says hey there partner! Read all <a href=\"/rango/about/\">About</a> us.")

def about(response):
    return HttpResponse("Rango says here is the about page. Let's go <a href=\"/rango/\">Index</a>.")
