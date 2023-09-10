from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def index(request):
    if not request.user.is_authenticated:
        return render(request, "login/index.html")
    else:
        return HttpResponseRedirect(reverse("home"))


def base(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, "login/index.html", {
                "message": "Invalid Username or Password! Try again"
                })
        else:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        return HttpResponseRedirect(reverse("home"))


def new_user(request):
    if request.method == "POST":
        user_name = request.POST["username"]
        pass_word = request.POST["passkey"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        if len(pass_word) < 8:
            return render(request, "login/new_user.html", {
                "message": "Password lenght is too short"
            })
        try:
            user = User.objects.create_user(user_name, '', pass_word)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
        except:
            return render(request, "login/new_user.html", {
                "message": "Username is taken! "
            })
    if not request.user.is_authenticated:
        return render(request, "login/new_user.html")
    else:
        return HttpResponseRedirect(reverse("home"))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))
