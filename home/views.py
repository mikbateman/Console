from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from . models import Loan, Expense, Investment


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "home/index.html")


def loan(request):
    if request.method == "POST":
        user = request.user.username
        name = request.POST["name"]
        principle = request.POST["principle"]
        interest = request.POST["interest"]
        tenure = request.POST["tenure"]
        emi = request.POST["emi"]
        start = request.POST["start"]
        end = request.POST["end"]
        l = Loan(user = user, name = name, principle = principle, interest = interest, tenure = tenure, emi = emi, start = start, end = end)
        l.save()
    return HttpResponseRedirect(reverse("home"))

def expense(request):
    if request.method == "POST":
        user = request.user.username
        year = int(request.POST["year"])
        month = int(request.POST["month"])
        income = int(request.POST["income"])
        utilities = int(request.POST["utilities"])
        food = int(request.POST["food"])
        entertainment = int(request.POST["entertainment"])
        groceries = int(request.POST["groceries"])
        subscriptions = int(request.POST["subscriptions"])
        emi = int(request.POST["emi"])
        unknown = int(request.POST["unknown"])
        balance = income - utilities - food - entertainment - groceries - subscriptions - emi - unknown
        e = Expense(user = user, year = year, month = month, income = income, utilities = utilities, food = food, entertainment = entertainment, groceries = groceries, subscriptions = subscriptions, emis = emi, something = unknown, balance = balance)
        e.save()
    return HttpResponseRedirect(reverse("home"))


def investment(request):
    if request.method == "POST":
        user = request.user.username
        year = int(request.POST["year"])
        month = int(request.POST["month"])
        stocks = int(request.POST["stocks"])
        mf = int(request.POST["mf"])
        gold = int(request.POST["gold"])
        assets = int(request.POST["assets"])
        i = Investment(user = user, year = year, month = month, stocks = stocks, mf = mf, gold = gold, assets = assets)
        i.save()
    return HttpResponseRedirect(reverse("home"))
