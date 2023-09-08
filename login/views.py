from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate


def index(request):
    return render(request, "login/index.html")


def base(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, "login/index.html", {
                "message": "Invalid Username or Password! Try again"
                })
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    #else:
    #   return HttpResponceRedirct(reverse("home"))
