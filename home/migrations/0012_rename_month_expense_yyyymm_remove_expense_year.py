# Generated by Django 4.2.5 on 2023-10-02 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_expense_entertainment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='month',
            new_name='yyyymm',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='year',
        ),
    ]
