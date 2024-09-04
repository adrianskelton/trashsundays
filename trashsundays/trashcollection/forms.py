from django import forms
from .models import TrashCollection

class TrashCollectionForm(forms.ModelForm):
    class Meta:
        model = TrashCollection
        fields = ['user', 'bags_collected', 'latitude', 'longitude']  
