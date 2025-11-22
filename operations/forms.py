from django import forms
from .models import TowerPin, Tower

class TowerPinForm(forms.ModelForm):
    class Meta:
        model = TowerPin
        fields = [
            'tower', 'province', 'city', 'barangay',
            'latitude', 'longitude', 'contact', 'remarks', 'picture','picture1'
        ]
        widgets = {
            'latitude': forms.TextInput(attrs={'readonly': 'readonly'}),
            'longitude': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Only show towers that don't already have a TowerPin
        used_towers = TowerPin.objects.values_list('tower_id', flat=True)
        self.fields['tower'].queryset = Tower.objects.exclude(id__in=used_towers)
