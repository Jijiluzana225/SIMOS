from django import forms
from .models import TowerPin, Tower
from .utils import compress_image


class TowerPinForm(forms.ModelForm):

    STATUS_LIMITED_CHOICES = [
   
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

    def save(self, commit=True):
        instance = super().save(commit=False)

        if self.cleaned_data.get("picture"):
            instance.picture = compress_image(self.cleaned_data["picture"])

        if self.cleaned_data.get("picture1"):
            instance.picture1 = compress_image(self.cleaned_data["picture1"])
        
        if self.cleaned_data.get("construction_picture"):
            instance.construction_picture = compress_image(self.cleaned_data["construction_picture"])

        if self.cleaned_data.get("construction_picture1"):
            instance.construction_picture1 = compress_image(self.cleaned_data["construction_picture1"])
        
        if self.cleaned_data.get("instrumentation_picture"):
            instance.instrumentation_picture = compress_image(self.cleaned_data["instrumentation_picture"])

        if self.cleaned_data.get("instrumentation_picture1"):
            instance.instrumentation_picture1 = compress_image(self.cleaned_data["instrumentation_picture1"])

        if commit:
            instance.save()
        return instance
    
    

from django import forms
from .models import TowerPin



class BictoUpdateForm(forms.ModelForm):

    STATUS_LIMITED_CHOICES = [
        ("Surveyed", "Surveyed"),
    ]

    class Meta:
        model = TowerPin
        fields = [
            "latitude",
            "longitude",
            "contact",
            "remarks",
            "picture",
            "picture1",
            "status",
        ]

        widgets = {
            "latitude": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Latitude",
                    
                }
            ),
            "longitude": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Longitude",
                  
                }
            ),
            "contact": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter contact person...",
                }
            ),
            "remarks": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Enter remarks...",
                }
            ),
            "picture": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/*",
                }
            ),
            "picture1": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/*",
                }
            ),
            "status": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["status"].choices = self.STATUS_LIMITED_CHOICES

    def save(self, commit=True):
        instance = super().save(commit=False)

        if self.cleaned_data.get("picture"):
            instance.picture = compress_image(self.cleaned_data["picture"])

        if self.cleaned_data.get("picture1"):
            instance.picture1 = compress_image(self.cleaned_data["picture1"])

        if commit:
            instance.save()

        return instance


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

    def save(self, commit=True):
        instance = super().save(commit=False)

        if self.cleaned_data.get("picture"):
            instance.picture = compress_image(self.cleaned_data["picture"])

        if self.cleaned_data.get("picture1"):
            instance.picture1 = compress_image(self.cleaned_data["picture1"])
        
        if self.cleaned_data.get("construction_picture"):
            instance.construction_picture = compress_image(self.cleaned_data["construction_picture"])

        if self.cleaned_data.get("construction_picture1"):
            instance.construction_picture1 = compress_image(self.cleaned_data["construction_picture1"])
        
        if self.cleaned_data.get("instrumentation_picture"):
            instance.instrumentation_picture = compress_image(self.cleaned_data["instrumentation_picture"])

        if self.cleaned_data.get("instrumentation_picture1"):
            instance.instrumentation_picture1 = compress_image(self.cleaned_data["instrumentation_picture1"])

        if commit:
            instance.save()
        return instance
    
class ElectricianUpdateForm(forms.ModelForm):

    # Only allow these two statuses
    STATUS_LIMITED_CHOICES = [
        ("Electrified", "Electrified"),
        ("Not Electrified", "Not Electrified"),
     
    ]

    class Meta:
        model = TowerPin
        fields = [
            "electrician_remarks",
            "electrician_picture",
            "electrician_picture1",
            "status",
        ]
        exclude = [
            "tower", "province", "city", "barangay",
            "latitude", "longitude", "contact", "remarks",
            "picture", "picture1", "created_by", "timestamp"
        ]
        widgets = {
            "electrician_remarks": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Enter Electrician remarks..."
                }
            ),
            "electrician_picture": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/*"
                }
            ),
            "electrician_picture1": forms.ClearableFileInput(
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

    def save(self, commit=True):
        instance = super().save(commit=False)


        
        if self.cleaned_data.get("electrician_picture"):
            instance.electrician_picture = compress_image(self.cleaned_data["electrician_picture"])

        if self.cleaned_data.get("electrician_picture1"):
            instance.electrician_picture1 = compress_image(self.cleaned_data["electrician_picture1"])
        
        if commit:
            instance.save()
        return instance

    
from django import forms
from .models import TowerPin

class InstrumentationUpdateForm(forms.ModelForm):

    # Allowed status options
    STATUS_LIMITED_CHOICES = [
        ("Instrumentation", "Instrumentation"),
        ("Completed", "Completed"),
        ("Up and Running", "Up and Running"),
        ("For Repair", "For Repair"),
        ("Up but Standby", "Up but Standby"),
    ]

    class Meta:
        model = TowerPin
        fields = [
            "instrumentation_remarks",
            "instrumentation_picture",
            "instrumentation_picture1",
            "technical_notes",
            "status",
        ]
        exclude = [
            "tower", "province", "city", "barangay",
            "latitude", "longitude", "contact", "remarks",
            "picture", "picture1", "created_by", "timestamp",
            "construction_picture", "construction_picture1",
            "contruction_remarks"
        ]
        widgets = {
            "instrumentation_remarks": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Enter instrumentation remarks..."
                }
            ),
            "technical_notes": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Enter technical notes..."
                }
            ),
            "instrumentation_picture": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/*"
                }
            ),
            "instrumentation_picture1": forms.ClearableFileInput(
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

    # Correct placement & proper overriding
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].choices = self.STATUS_LIMITED_CHOICES

    def save(self, commit=True):
        instance = super().save(commit=False)

        if self.cleaned_data.get("picture"):
            instance.picture = compress_image(self.cleaned_data["picture"])

        if self.cleaned_data.get("picture1"):
            instance.picture1 = compress_image(self.cleaned_data["picture1"])
        
        if self.cleaned_data.get("construction_picture"):
            instance.construction_picture = compress_image(self.cleaned_data["construction_picture"])

        if self.cleaned_data.get("construction_picture1"):
            instance.construction_picture1 = compress_image(self.cleaned_data["construction_picture1"])
        
        if self.cleaned_data.get("instrumentation_picture"):
            instance.instrumentation_picture = compress_image(self.cleaned_data["instrumentation_picture"])

        if self.cleaned_data.get("instrumentation_picture1"):
            instance.instrumentation_picture1 = compress_image(self.cleaned_data["instrumentation_picture1"])

        if commit:
            instance.save()
        return instance