from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "home/index.html")
