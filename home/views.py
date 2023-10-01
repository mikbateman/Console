from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Sum
from datetime import datetime
from . models import Loan, Expense, Investment
from . core import simple, cat, bar


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

d = ["0", 0, 0, 0, 0]

def expense(request):
    if request.method == "POST":
        user = request.user.username
        year = int(request.POST["year"])
        month = int(request.POST["month"])
        income = int(request.POST["income"])
        utilities = int(request.POST["utilities"])
        shoping = int(request.POST["shoping"])
        fuel = int(request.POST["fuel"])
        food = int(request.POST["food"])
        groceries = int(request.POST["groceries"])
        subscriptions = int(request.POST["subscriptions"])
        emi = int(request.POST["emi"])
        unknown = int(request.POST["unknown"])
        d[0] = str(request.POST["msg"])
        balance = income - utilities - food - groceries - subscriptions - emi - unknown - shoping - fuel
        e = Expense(user = user, year = year, month = month, income = income, utilities = utilities, food = food, groceries = groceries, subscriptions = subscriptions, emis = emi, something = unknown, shoping = shoping, fuel = fuel, balance = balance)
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
        if len(str(month)) == 1:
            yyyymm = str(year) + "0" + str(month)
        else:
            yyyymm = str(year) + str(month)
        i = Investment(user = user, yyyymm = yyyymm, stocks = stocks, mf = mf, gold = gold, assets = assets)
        i.save()
    return HttpResponseRedirect(reverse("home"))


def report(request):
    if request.method == "POST":
        user = request.user.username
        d[1] = user
        year = int(request.POST["year"])
        month = int(request.POST["month"])

        loan_total = 0
        loan_paid = 0

        if len(str(month)) == 1:
            yyyymm = str(year) + "0" + str(month)
        else:
            yyyymm = str(year) + str(month)

        loans = Loan.objects.filter(user=user)
        exp = Expense.objects.filter(user=user, month=month, year=year)
        inv = Investment.objects.filter(user=user, yyyymm=int(yyyymm))

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
            d[1] = f"/static/data/loans/{user}.png"
        else:
            loan_msg = 0

        if exp.exists():
            exp = exp[0]
            expenses = exp.utilities + exp.food + exp.something + exp.emis + exp.groceries + exp.subscriptions + exp.fuel + exp.shoping
            balance = exp.balance
            exp_pie = simple("Expenditure", balance, expenses)
            exp_pie.savefig(f"home/static/data/exp/{user}_{exp_name}", dpi=300)
            d[2] = f"/static/data/exp/{user}_{exp_name}.png"
            cat_pie = cat(exp.utilities, exp.food, exp.fuel, exp.shoping, exp.groceries, exp.subscriptions, exp.emis, exp.something)
            cat_pie.savefig(f"home/static/data/category/{user}_{exp_name}", dpi=300)
            d[3] = f"/static/data/category/{user}_{exp_name}.png"
        else:
            exp = 0

        if inv.exists():
            inv = inv[0]
            tmp = Investment.objects.filter(yyyymm__lt = inv.yyyymm).aggregate(stocks = Sum("stocks"), mf = Sum("mf"), gold = Sum("gold"), assets = Sum("assets"))
            l1 = [int(inv.stocks), int(inv.mf), int(inv.gold), int(inv.assets)]
            l2 = [int(tmp["stocks"]), int(tmp["mf"]), int(tmp["gold"]), int(tmp["assets"])]
            inv_bar = bar(l1, l2)
            inv_bar.savefig(f"home/static/data/inv/{user}_{exp_name}", dpi=300)
        else:
            tmp = Investment.objects.filter(yyyymm__lt = int(exp_name)).aggregate(stocks = Sum("stocks"), mf = Sum("mf"), gold = Sum("gold"), assets = Sum("assets"))
            l1 = [0, 0, 0, 0]
            l2 = [tmp["stocks"], tmp["mf"], tmp["gold"], tmp["assets"]]
            inv_bar = bar(l1, l2)
            inv_bar.savefig(f"home/static/data/inv/{user}_{exp_name}", dpi=300)

        d[4] = f"/static/data/inv/{user}_{exp_name}.png"

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
            "msg": d[0],
            "floan": d[1],
            "fexp": d[2],
            "fcat": d[3],
            "finv": d[4],
            "total": expenses
            })
