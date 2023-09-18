from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Sum
from datetime import datetime
from . models import Loan, Expense, Investment
from . core import simple, cat


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "home/index.html")


def loan(request):
    if request.method == "POST":
        user = request.user.username
        name = request.POST["name"]
        tenure = request.POST["tenure"]
        emi = request.POST["emi"]
        start = request.POST["start"]
        l = Loan(user = user, name = name, tenure = tenure, emi = emi, start = start)
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


def report(request):
    if request.method == "POST":
        user = request.user.username
        year = int(request.POST["year"])
        month = int(request.POST["month"])
        loan_total = 0
        loan_paid = 0
        loans = Loan.objects.filter(user=user)
        exp = Expense.objects.filter(user=user, month=month, year=year)
        curr = str(datetime.now().date()).split("-")
        if loans.exists():
            for i in loans:
                loan_total += i.tenure * i.emi
                start = str(i.start).split("-")
                paid = (int(curr[0]) - int(start[0])) * 12 + int(curr[1]) - int(start[1])
                loan_paid += paid * i.emi
        else:
            print("No Loans")
        if exp.exists():
            exp = exp[0]
            expenses = exp.utilities + exp.food + exp.entertainment + exp.something + exp.emis + exp.groceries + exp.subscriptions
            balance = exp.balance
        else:
            print("Not enough Data")
        l = simple("Loans", loan_paid, loan_total - loan_paid)
        if len(str(month)) == 1:
            name = str(year) + "0" + str(month)
        else:
            name = str(year) + str(month)
        l.savefig(f"data/loans/{user}", dpi=300)
        # simple("Expenditure", balance, expenses)
        # cat(exp.utilities, exp.food, exp.entertainment, exp.groceries, exp.subscriptions, exp.emis, exp.something)
        return HttpResponseRedirect(reverse("home"))
