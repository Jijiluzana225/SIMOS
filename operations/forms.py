from django import forms
from .models import TowerPin, Tower  # make sure you import Tower

class TowerPinForm(forms.ModelForm):
    class Meta:
        model = TowerPin
        fields = [
            'tower', 'province', 'city', 'barangay',
            'latitude', 'longitude', 'contact', 'remarks', 'picture', 'picture1'
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
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Get all Tower IDs that are already in TowerPin
        used_tower_ids = TowerPin.objects.values_list('tower_id', flat=True)
        # Filter the tower dropdown to only show towers not in TowerPin
        self.fields['tower'].queryset = Tower.objects.exclude(id__in=used_tower_ids)
