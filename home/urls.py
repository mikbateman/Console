from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("loan", views.loan, name="loan"),
    path("expenses", views.expense, name="expenses"),
    path("investments", views.investment, name="investments"),
    path("report", views.report, name="report"),
]
