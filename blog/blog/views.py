from django.http import HttpRequest, HttpResponse,HttpResponseRedirect
from django.shortcuts import render


def helloWorld(request:HttpRequest) -> HttpResponse:
    return HttpResponse(content="Hello World")


def home(request:HttpRequest) -> HttpResponse:
    return render(request=request, template_name="home.html", context={"username": "User"})


def about(request:HttpRequest) -> HttpResponse:
    return render(request=request, template_name="about.html")


def google(request:HttpRequest) -> HttpResponseRedirect:
    return HttpResponseRedirect(redirect_to="https://www.google.com")
