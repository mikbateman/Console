# Generated by Django 4.2.5 on 2023-09-30 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_loan_end_remove_loan_interest_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='shoping',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
