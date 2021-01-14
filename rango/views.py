from django.http import HttpResponse

def index(response):
    return HttpResponse("Rango says hey there partner!")
