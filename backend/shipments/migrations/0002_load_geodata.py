# Generated by Django 4.2.1 on 2023-05-17 18:38

from django.db import migrations
import csv


def load_geodata(apps, schema_editor):
    Country = apps.get_model("shipments", "Country")
    City = apps.get_model("shipments", "City")

    with open('geodata.csv') as f:
        reader = csv.reader(f)
        data = list(reader)

    City.objects.all().delete()
    Country.objects.all().delete()

    Country.objects.bulk_create(
        [Country(name=country) for country in set([row[0] for row in data])]
    )
    countries = {country.name: country for country in Country.objects.all()}

    City.objects.bulk_create(
        [City(name=city, country=countries[country]) for country, city in data]
    )


def reverse_load_geodata(apps, schema_editor):
    Country = apps.get_model("shipments", "Country")
    City = apps.get_model("shipments", "City")

    City.objects.all().delete()
    Country.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_geodata,
                             reverse_load_geodata)
    ]
