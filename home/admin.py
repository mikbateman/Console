from django.contrib import admin
from . models import Loan, Expense, Investment


admin.site.register(Loan)
admin.site.register(Expense)
admin.site.register(Investment)
