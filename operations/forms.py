from django import forms
from .models import TowerPin

class TowerPinForm(forms.ModelForm):
    class Meta:
        model = TowerPin
        fields = [
            'tower', 'province', 'city', 'barangay',
            'latitude', 'longitude', 'remarks', 'picture'
        ]

        widgets = {
            'latitude': forms.TextInput(attrs={'readonly': 'readonly'}),
            'longitude': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
