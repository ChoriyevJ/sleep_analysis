# Generated by Django 4.2.7 on 2024-03-15 00:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_country_currency_doctordetail_doctorexperience_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="phone",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]