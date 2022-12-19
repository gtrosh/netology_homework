from csv import DictReader

from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse("bus_stations"))


file_path = settings.BUS_STATION_CSV
with open(file_path, encoding="utf-8") as csvfile:
    reader = DictReader(csvfile)
    STATIONS = [
        {"Name": row["Name"], "Street": row["Street"], "District": row["District"]}
        for row in reader
    ]


def bus_stations(request):
    page_num = request.GET.get("page", 1)
    paginator = Paginator(STATIONS, 10)
    page = paginator.get_page(page_num)
    bus_stations = page.object_list
    context = {
        "bus_stations": bus_stations,
        "page": page,
    }
    return render(request, "stations/index.html", context)
