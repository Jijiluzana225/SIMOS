from django.contrib.auth.decorators import login_required
from django.shortcuts import render

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

@login_required(login_url='login')
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
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def view_towers(request):
    provinces = Province.objects.all()
    
    # Check if user can survey (BICTO group)
    can_survey = request.user.is_authenticated and request.user.groups.filter(name="BICTO").exists()
    
    # Check if user can update construction (Construction group)
    user_can_update = request.user.is_authenticated and request.user.groups.filter(name="CONSTRUCTION").exists()

    can_power_up = request.user.is_authenticated and request.user.groups.filter(name="INSTRUMENTATION").exists()
    
    return render(request, "operations/view_towers.html", {
        "provinces": provinces,
        "can_survey": can_survey,
        "user_can_update": user_can_update,
        "can_power_up": can_power_up,

    })



@login_required(login_url='login')
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
            "picture_url": t.picture.url,
            "status": t.status
        }
        for t in towers
    ]
    return JsonResponse(data, safe=False)

@login_required(login_url='login')
def landing_page(request):
    """
    Display the landing page with login/dashboard button.
    """
    return render(request, "operations/landing.html")


from django.shortcuts import render, redirect, get_object_or_404
from .models import TowerPin
from .forms import ConstructionUpdateForm
def update_construction(request, pin_id):
    towerpin = get_object_or_404(TowerPin, id=pin_id)

    if request.method == "POST":
        form = ConstructionUpdateForm(request.POST, request.FILES, instance=towerpin)
        if form.is_valid():
            form.save()
            return redirect("view_towers")  # adjust to your page
    else:
        form = ConstructionUpdateForm(instance=towerpin)

    return render(request, "operations/construction.html", {
        "form": form,
        "towerpin": towerpin
    })


from django.shortcuts import render, redirect, get_object_or_404
from .models import TowerPin
from .forms import InstrumentationUpdateForm
def update_instrumentation(request, pin_id):
    towerpin = get_object_or_404(TowerPin, id=pin_id)

    if request.method == "POST":
        form = InstrumentationUpdateForm(request.POST, request.FILES, instance=towerpin)
        if form.is_valid():
            form.save()
            return redirect("view_towers")  # adjust to your page
    else:
        form = InstrumentationUpdateForm(instance=towerpin)

    return render(request, "operations/instrumentation.html", {
        "form": form,
        "towerpin": towerpin
    })



from django.shortcuts import render, get_object_or_404
from .models import TowerPin

def tower_details_view(request, tower_id):
    tower_pin = get_object_or_404(TowerPin, id=tower_id)
    return render(request, 'operations/tower_details.html', {'tower_pin': tower_pin})
