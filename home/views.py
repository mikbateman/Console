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

        if len(str(month)) == 1:
            exp_name = str(year) + "0" + str(month)
        else:
            exp_name = str(year) + str(month)

        if loans.exists():
            loan_msg = []
            for i in loans:
                tmp = i.tenure * i.emi
                loan_total += tmp
                start = str(i.start).split("-")
                paid = (int(curr[0]) - int(start[0])) * 12 + int(curr[1]) - int(start[1])
                loan_paid += paid * i.emi
                loan_msg.append(f"{i.name} : {tmp}")
            loan_pie = simple("Loans", loan_paid, loan_total - loan_paid)
            loan_pie.savefig(f"home/static/data/loans/{user}", dpi=300)
        else:
            loan_msg = "You don't have any loans"

        if exp.exists():
            exp = exp[0]
            expenses = exp.utilities + exp.food + exp.entertainment + exp.something + exp.emis + exp.groceries + exp.subscriptions
            balance = exp.balance
            exp_pie = simple("Expenditure", balance, expenses)
            exp_pie.savefig(f"home/static/data/exp/{user}_{exp_name}", dpi=300)
            cat_pie = cat(exp.utilities, exp.food, exp.entertainment, exp.groceries, exp.subscriptions, exp.emis, exp.something)
            cat_pie.savefig(f"home/static/data/category/{user}_{exp_name}", dpi=300)
        else:
            exp_msg = "Not enough data to obtain report"

        months = {
                1: "January",
                2: "February",
                3: "March",
                4: "April",
                5: "May",
                6: "June",
                7: "July",
                8: "August",
                9: "September",
                10: "October",
                11: "November",
                12: "December"
                }
        return render(request, "home/report.html", {
            "month": f"{months[month]}-{year}",
            "loan": loan_msg,
            "exp": exp,
            "total": expenses,
            })
