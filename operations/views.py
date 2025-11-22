from django.shortcuts import render, redirect
from .models import TowerPin, Tower
from .forms import TowerPinForm

def home(request):
    pins = TowerPin.objects.select_related("tower")
    return render(request, 'operations/home.html', {"pins": pins})


def add_pin(request):
    if request.method == 'POST':
        form = TowerPinForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TowerPinForm()

    return render(request, 'locations/add_pin.html', {"form": form})


from django.shortcuts import render, redirect
from .models import TowerPin
from .forms import TowerPinForm

def home(request):
    pins = TowerPin.objects.all()
    if request.method == "POST":
        form = TowerPinForm(request.POST, request.FILES)
        if form.is_valid():
            tower_pin = form.save(commit=False)
            tower_pin.created_by = request.user  # set the current user
            tower_pin.save()
    else:
        form = TowerPinForm()

    return render(request, "operations/home.html", {"pins": pins, "form": form})


# views.py
from django.http import JsonResponse
from .models import TowerPin

def towers_by_province(request, province_id):
    towers = TowerPin.objects.filter(province_id=province_id)
    data = [
        {"name": t.tower.name, "latitude": t.latitude, "longitude": t.longitude}
        for t in towers
    ]
    return JsonResponse(data, safe=False)


def location(request):
    pins = TowerPin.objects.all()

    if request.method == "POST":
        form = TowerPinForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = TowerPinForm()

    return render(request, "operations/location.html", {"pins": pins, "form": form})


from django.shortcuts import render
from django.http import JsonResponse
from .models import Province, TowerPin
def view_towers(request):
    provinces = Province.objects.all()
    can_survey = request.user.is_authenticated and request.user.groups.filter(name="BICTO").exists()
    return render(request, "operations/view_towers.html", {"provinces": provinces, "can_survey": can_survey})


# API endpoint to fetch towers for a specific province
def towers_by_province(request, province_id):
    towers = TowerPin.objects.filter(province_id=province_id)
    data = [
        {
            "id": t.id,
            "name": t.tower.name,
            "latitude": t.latitude,
            "longitude": t.longitude,
            "contact": t.contact,
            "picture_url": t.picture.url
        }
        for t in towers
    ]
    return JsonResponse(data, safe=False)

def landing_page(request):
    """
    Display the landing page with login/dashboard button.
    """
    return render(request, "operations/landing.html")