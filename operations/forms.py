from django import forms
from .models import TowerPin, Tower

class TowerPinForm(forms.ModelForm):

    STATUS_LIMITED_CHOICES = [
        ("Scheduled", "Scheduled"),
        ("Rescheduled", "Rescheduled"),
        ("Surveyed", "Surveyed"),
    ]

    class Meta:
        model = TowerPin
        fields = [
            'tower', 'province', 'city', 'barangay',
            'latitude', 'longitude', 'contact',
            'remarks', 'picture', 'picture1', 'status'
        ]
        widgets = {
            'tower': forms.Select(attrs={'class': 'form-select'}),
            'province': forms.Select(attrs={'class': 'form-select'}),
            'city': forms.Select(attrs={'class': 'form-select'}),
            'barangay': forms.Select(attrs={'class': 'form-select'}),
            'latitude': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'longitude': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'contact': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter contact name and number...'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter remarks...'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'picture1': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            # placeholder, real override is in __init__
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # ✔ Override status choices here (safe and correct)
        self.fields['status'].choices = self.STATUS_LIMITED_CHOICES

        # ✔ Filter towers: show only towers not yet used in TowerPin
        used_tower_ids = TowerPin.objects.values_list('tower_id', flat=True)
        self.fields['tower'].queryset = Tower.objects.exclude(id__in=used_tower_ids)

from django import forms
from .models import TowerPin

class ConstructionUpdateForm(forms.ModelForm):

    # Only allow these two statuses
    STATUS_LIMITED_CHOICES = [
        ("On Going Construction", "On Going Construction"),
        ("Surveyed", "Surveyed"),
    ]

    class Meta:
        model = TowerPin
        fields = [
            "contruction_remarks",
            "construction_picture",
            "construction_picture1",
            "status",
        ]
        exclude = [
            "tower", "province", "city", "barangay",
            "latitude", "longitude", "contact", "remarks",
            "picture", "picture1", "created_by", "timestamp"
        ]
        widgets = {
            "contruction_remarks": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Enter construction remarks..."
                }
            ),
            "construction_picture": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/*"
                }
            ),
            "construction_picture1": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/*"
                }
            ),
            "status": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
        }

    # Correctly override status choices
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].choices = self.STATUS_LIMITED_CHOICES
