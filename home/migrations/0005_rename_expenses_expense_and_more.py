# Generated by Django 4.2.5 on 2023-09-12 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_other_expenses_something'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Expenses',
            new_name='Expense',
        ),
        migrations.RenameModel(
            old_name='Investments',
            new_name='Investment',
        ),
        migrations.RenameModel(
            old_name='Loans',
            new_name='Loan',
        ),
    ]
