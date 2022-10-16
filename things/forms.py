"""Forms of the project."""
from django import forms
from .models import Thing
# Create your forms here.
class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        labels = { 'name': 'Name', 'description': 'Description', 'quantity': 'Thing' }
        widgets = { 'description': forms.Textarea(), 'quantity': forms.NumberInput() }

    # def clean(self):
    #     super().clean()
    #     name = self.cleaned_data.get('name')
    #     copy =
