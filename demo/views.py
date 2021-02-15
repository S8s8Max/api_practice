from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Data
import pandas as pd
import random

def index(request):
    Data.objects.all().delete()
    df_csv = pd.read_csv("static/demo/csv/LendingInterestRate.csv")

    for row in df_csv.iterrows():
        for i in range(1980,2021):
            year = i
            country = row[1][0]
            interest_rate = row[1][f"{i}"]

            data, created = Data.objects.get_or_create(
                country=country,
                year=year,
                interest_rate=interest_rate
            )
            data.save()

    BRN = Data.objects.filter(country="BRN")
    IDN = Data.objects.filter(country="IDN")
    KHM = Data.objects.filter(country="KHM")
    LAO = Data.objects.filter(country="LAO")
    MMR = Data.objects.filter(country="MMR")
    MYS = Data.objects.filter(country="MYS")
    PHL = Data.objects.filter(country="PHL")
    SGP = Data.objects.filter(country="SGP")
    THA = Data.objects.filter(country="THA")
    TLS = Data.objects.filter(country="TLS")
    VNM = Data.objects.filter(country="VNM")

    BRN_interest_rate = [None or "" if x.interest_rate == None else x.interest_rate for x in BRN]
    IDN_interest_rate = [None or "" if x.interest_rate == None else x.interest_rate for x in IDN]
    KHM_interest_rate = [None or "" if x.interest_rate == None else x.interest_rate for x in KHM]
    LAO_interest_rate = [None or "" if x.interest_rate == None else x.interest_rate for x in LAO]
    MMR_interest_rate = [None or "" if x.interest_rate == None else x.interest_rate for x in MMR]
    MYS_interest_rate = [None or "" if x.interest_rate == None else x.interest_rate for x in MYS]
    PHL_interest_rate = [None or "" if x.interest_rate == None else x.interest_rate for x in PHL]
    SGP_interest_rate = [None or "" if x.interest_rate == None else x.interest_rate for x in SGP]
    THA_interest_rate = [None or "" if x.interest_rate == None else x.interest_rate for x in THA]
    TLS_interest_rate = [None or "" if x.interest_rate == None else x.interest_rate for x in TLS]
    VNM_interest_rate = [None or "" if x.interest_rate == None else x.interest_rate for x in VNM]

    params = {
        "data": {
            "BRN": {
                "country": "Burnei",
                "interest_rate": BRN_interest_rate,
                "color": colorPicker(),
            },
            "IDN": {
                "country": "Indonesia",
                "interest_rate": IDN_interest_rate,
                "color": colorPicker(),
            },
            "KHM": {
                "country": "Cambodia",
                "interest_rate": KHM_interest_rate,
                "color": colorPicker(),
            },
            "LAO": {
                "country": "Laos",
                "interest_rate": LAO_interest_rate,
                "color": colorPicker(),
            },
            "MMR": {
                "country": "Myanmer",
                "interest_rate": MMR_interest_rate,
                "color": colorPicker(),
            },
            "MYS": {
                "country": "Malysia",
                "interest_rate": MYS_interest_rate,
                "color": colorPicker(),
            },
            "PHL": {
                "country": "Philippines",
                "interest_rate": PHL_interest_rate,
                "color": colorPicker(),
            },
            "SGP": {
                "country": "Singapore",
                "interest_rate": SGP_interest_rate,
                "color": colorPicker(),
            },
            "THA": {
                "country": "Thailand",
                "interest_rate": THA_interest_rate,
                "color": colorPicker(),
            },
            "TLS": {
                "country": "East Timor",
                "interest_rate": TLS_interest_rate,
                "color": colorPicker(),
            },
            "VNM": {
                "country": "Vietnam",
                "interest_rate": VNM_interest_rate,
                "color": colorPicker(),
            },
        }
    }
    return render(request, "demo/index.html", params)

def colorPicker():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = "rgb(" + str(r) + ", " + str(g) + ", " + str(b) + ")"
    return color
